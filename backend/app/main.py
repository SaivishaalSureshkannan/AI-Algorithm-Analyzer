from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ast
from typing import Dict, List, Optional
import joblib
import os
import sys
from pathlib import Path
import json

# Add the ml_model directory to Python path
backend_dir = Path(__file__).parent.parent
ml_model_dir = backend_dir / "ml_model"
sys.path.append(str(ml_model_dir))

from src.feature_extractor import FeatureExtractor

# Load the ML model
model_path = backend_dir / "ml_model" / "models" / "complexity_predictor.joblib"
model = joblib.load(model_path)
feature_extractor = FeatureExtractor()

# Load feature stats
stats_path = Path(__file__).parent.parent / "ml_model" / "src" / "feature_stats.json"
with open(stats_path, "r") as f:
    feature_stats = json.load(f)

app = FastAPI(title="AI Algorithm Complexity Analyzer")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeAnalysisRequest(BaseModel):
    code: str

class CodeAnalysisResponse(BaseModel):
    complexity: str
    loops: Dict[str, int]
    recursion: bool
    suggestions: List[str]

class MLPredictionRequest(BaseModel):
    code: str

class MLPredictionResponse(BaseModel):
    predicted_complexity: str
    confidence: float
    features: Dict[str, int]

def analyze_code(code: str) -> CodeAnalysisResponse:
    try:
        # Parse the code into an AST
        tree = ast.parse(code)
        
        # Initialize counters
        loop_count = {
            "for_loops": 0,
            "while_loops": 0
        }
        has_recursion = False
        
        # Analyze the AST
        for node in ast.walk(tree):
            if isinstance(node, ast.For):
                loop_count["for_loops"] += 1
            elif isinstance(node, ast.While):
                loop_count["while_loops"] += 1
            elif isinstance(node, ast.FunctionDef):
                # Check for recursion by looking for function calls with the same name
                for child in ast.walk(node):
                    if isinstance(child, ast.Call) and isinstance(child.func, ast.Name):
                        if child.func.id == node.name:
                            has_recursion = True
        
        # Determine complexity based on simple rules
        complexity = "O(1)"
        suggestions = []
        
        if loop_count["for_loops"] > 0 or loop_count["while_loops"] > 0:
            if loop_count["for_loops"] + loop_count["while_loops"] > 1:
                complexity = "O(n²)"
                suggestions.append("Consider optimizing nested loops")
            else:
                complexity = "O(n)"
        
        if has_recursion:
            complexity = "O(2ⁿ)"
            suggestions.append("Consider using iteration instead of recursion for better performance")
        
        return CodeAnalysisResponse(
            complexity=complexity,
            loops=loop_count,
            recursion=has_recursion,
            suggestions=suggestions
        )
    
    except SyntaxError as e:
        raise HTTPException(status_code=400, detail=f"Invalid Python code: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error analyzing code: {str(e)}")

@app.post("/analyze", response_model=CodeAnalysisResponse)
async def analyze_algorithm(request: CodeAnalysisRequest):
    """
    Analyze Python code and return its complexity analysis
    """
    return analyze_code(request.code)

def is_outlier(features):
    # Heuristic 1: Suspicious patterns
    if features['for_loops'] >= 3 or features['while_loops'] >= 2:
        return True
    if features['has_recursion'] and features['recursive_calls'] >= 3:
        return True

    # Heuristic 2: Out of training range or z-score
    for key, value in features.items():
        if key in feature_stats:
            if value < feature_stats[key]['min'] or value > feature_stats[key]['max']:
                return True
            # Optional: z-score check for continuous features
            if feature_stats[key]['std'] > 0:
                z = abs((value - feature_stats[key]['mean']) / feature_stats[key]['std'])
                if z > 3:  # 3-sigma rule
                    return True
    return False

@app.post("/predict", response_model=MLPredictionResponse)
async def predict_complexity(request: MLPredictionRequest):
    """
    Predict the time complexity of Python code using ML model
    """
    try:
        features = feature_extractor.extract_features(request.code)

        # Outlier/Heuristic detection
        if is_outlier(features):
            return MLPredictionResponse(
                predicted_complexity="Unknown",
                confidence=1.0,
                features=features
            )

        feature_vector = feature_extractor.get_feature_vector(request.code)
        probabilities = model.predict_proba([feature_vector])[0]
        confidence = float(max(probabilities))
        prediction = model.predict([feature_vector])[0]

        # Confidence fallback
        if confidence < 0.5:
            prediction = "Unknown"
            confidence = 1.0

        return MLPredictionResponse(
            predicted_complexity=prediction,
            confidence=confidence,
            features=features
        )
    except SyntaxError as e:
        raise HTTPException(status_code=400, detail=f"Invalid Python code: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error predicting complexity: {str(e)}")

@app.get("/")
async def root():
    return {"message": "AI Algorithm Complexity Analyzer API"} 