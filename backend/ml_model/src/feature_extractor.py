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
            'nested_loops': 0,  # Now: number of loops inside other loops
            'max_depth': 0,
            'has_recursion': 0,
            'input_vars': 0,
            'max_nesting': 0,
            'input_dependent_loops': 0,  # Only one feature for input-dependent loops
            'returns_in_loops': 0,       # New: count of return statements inside loops
            'calls_in_loops': 0,         # New: count of function calls inside loops
            'top_level_loops': 0         # New: number of top-level loops
        }
        self.input_args = set()
        self.current_function_name = None
    
    def extract_features(self, code: str) -> Dict[str, int]:
        """Extract features from Python code using AST."""
        try:
            tree = ast.parse(code)
            self._reset_features()
            self.input_args = set()
            self.current_function_name = None
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    self.input_args = {arg.arg for arg in node.args.args}
                    self.current_function_name = node.name
            self._analyze_ast(tree)
            return self.features
        except SyntaxError:
            raise ValueError("Invalid Python code")
    
    def _reset_features(self):
        """Reset all feature counters."""
        for key in self.features:
            self.features[key] = 0
    
    def _analyze_ast(self, node: ast.AST, depth: int = 0, nesting_level: int = 0, in_loop: bool = False, top_level: bool = True):
        """Recursively analyze AST nodes and extract features."""
        # Update max depth
        self.features['max_depth'] = max(self.features['max_depth'], depth)
        # Update max nesting level
        self.features['max_nesting'] = max(self.features['max_nesting'], nesting_level)
        # Count different types of nodes
        if isinstance(node, (ast.For, ast.While)):
            if nesting_level == 0:
                self.features['top_level_loops'] += 1
            if nesting_level > 0:
                self.features['nested_loops'] += 1
            if isinstance(node, ast.For):
                self.features['for_loops'] += 1
                if self._is_input_dependent_for(node):
                    self.features['input_dependent_loops'] += 1
            else:
                self.features['while_loops'] += 1
                if self._is_input_dependent_while(node):
                    self.features['input_dependent_loops'] += 1
            for child in node.body:
                self._analyze_ast(child, depth + 1, nesting_level + 1, in_loop=True, top_level=False)
        elif isinstance(node, ast.If):
            self.features['if_statements'] += 1
            for child in node.body:
                self._analyze_ast(child, depth + 1, nesting_level, in_loop=in_loop, top_level=False)
            for child in node.orelse:
                self._analyze_ast(child, depth + 1, nesting_level, in_loop=in_loop, top_level=False)
        elif isinstance(node, ast.Call):
            # Recursion detection
            if isinstance(node.func, ast.Name) and self.current_function_name and node.func.id == self.current_function_name:
                self.features['recursive_calls'] += 1
                self.features['has_recursion'] = 1
            if in_loop:
                self.features['calls_in_loops'] += 1
        elif isinstance(node, ast.Return):
            if in_loop:
                self.features['returns_in_loops'] += 1
        elif isinstance(node, ast.arg):
            self.features['input_vars'] += 1
        # Analyze other child nodes that aren't part of control structures
        if not isinstance(node, (ast.For, ast.While, ast.If)):
            for child in ast.iter_child_nodes(node):
                self._analyze_ast(child, depth + 1, nesting_level, in_loop=in_loop, top_level=False)
    
    def _is_input_dependent_for(self, node: ast.For) -> bool:
        # Check if the loop's range uses any input argument
        # Handles range(n), range(len(arr)), direct iteration over input, etc.
        if isinstance(node.iter, ast.Call):
            # e.g., range(n), range(len(arr)), etc.
            call = node.iter
            # Check arguments of the call
            for arg in ast.walk(call):
                if isinstance(arg, ast.Name) and arg.id in self.input_args:
                    return True
                if isinstance(arg, ast.Call) and hasattr(arg.func, 'id') and arg.func.id == 'len':
                    for sub_arg in arg.args:
                        if isinstance(sub_arg, ast.Name) and sub_arg.id in self.input_args:
                            return True
        elif isinstance(node.iter, ast.Name):
            # e.g., for x in arr:
            if node.iter.id in self.input_args:
                return True
        return False

    def _is_input_dependent_while(self, node: ast.While) -> bool:
        # Check if the while loop's condition uses any input argument
        for arg in ast.walk(node.test):
            if isinstance(arg, ast.Name) and arg.id in self.input_args:
                return True
        return False
    
    def get_feature_vector(self, code: str) -> np.ndarray:
        """Convert code to a feature vector."""
        features = self.extract_features(code)
        return np.array(list(features.values())) 