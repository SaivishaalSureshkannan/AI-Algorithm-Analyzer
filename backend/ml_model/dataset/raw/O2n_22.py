{
    "code": "def exponential_time_22(n):\n    # Generate all valid combinations of n pairs of parentheses\n    def backtrack(s, open_count, close_count, results):\n        if len(s) == 2 * n:\n            results.append(s)\n            return\n        if open_count < n:\n            backtrack(s + '(', open_count + 1, close_count, results)\n        if close_count < open_count:\n            backtrack(s + ')', open_count, close_count + 1, results)\n    results = []\n    backtrack('', 0, 0, results)\n    return results",
    "complexity": "O(2^n)"
}