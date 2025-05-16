import ast
from typing import Dict, List, Tuple
import numpy as np

class FeatureExtractor:
    def __init__(self):
        self.features = {
            'for_loops': 0,
            'while_loops': 0,
            'if_statements': 0,
            'recursive_calls': 0,
            'nested_loops': 0,
            'max_depth': 0,
            'has_recursion': 0,
            'input_vars': 0,
            'max_nesting': 0
        }
    
    def extract_features(self, code: str) -> Dict[str, int]:
        """Extract features from Python code using AST."""
        try:
            tree = ast.parse(code)
            self._reset_features()
            self._analyze_ast(tree)
            return self.features
        except SyntaxError:
            raise ValueError("Invalid Python code")
    
    def _reset_features(self):
        """Reset all feature counters."""
        for key in self.features:
            self.features[key] = 0
    
    def _analyze_ast(self, node: ast.AST, depth: int = 0, nesting_level: int = 0):
        """Recursively analyze AST nodes and extract features."""
        # Update max depth
        self.features['max_depth'] = max(self.features['max_depth'], depth)
        
        # Update max nesting level
        self.features['max_nesting'] = max(self.features['max_nesting'], nesting_level)
        
        # Count different types of nodes
        if isinstance(node, ast.For):
            self.features['for_loops'] += 1
            # Analyze the body of the for loop
            for child in node.body:
                self._analyze_ast(child, depth + 1, nesting_level + 1)
        elif isinstance(node, ast.While):
            self.features['while_loops'] += 1
            # Analyze the body of the while loop
            for child in node.body:
                self._analyze_ast(child, depth + 1, nesting_level + 1)
        elif isinstance(node, ast.If):
            self.features['if_statements'] += 1
            # Analyze the body of the if statement
            for child in node.body:
                self._analyze_ast(child, depth + 1, nesting_level)
            # Analyze the else body if it exists
            for child in node.orelse:
                self._analyze_ast(child, depth + 1, nesting_level)
        elif isinstance(node, ast.Call):
            # Check for recursive calls
            if isinstance(node.func, ast.Name):
                self.features['recursive_calls'] += 1
                self.features['has_recursion'] = 1
        elif isinstance(node, ast.arg):
            self.features['input_vars'] += 1
        
        # Analyze other child nodes that aren't part of control structures
        if not isinstance(node, (ast.For, ast.While, ast.If)):
            for child in ast.iter_child_nodes(node):
                self._analyze_ast(child, depth + 1, nesting_level)
    
    def get_feature_vector(self, code: str) -> np.ndarray:
        """Convert code to a feature vector."""
        features = self.extract_features(code)
        return np.array(list(features.values())) 