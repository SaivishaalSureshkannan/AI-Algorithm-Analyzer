from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ast
from typing import Dict, List, Optional

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

@app.get("/")
async def root():
    return {"message": "AI Algorithm Complexity Analyzer API"} 