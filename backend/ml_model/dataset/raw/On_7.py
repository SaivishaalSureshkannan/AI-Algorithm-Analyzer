{
    "code": "def linear_time_7(n):\n    if n <= 1:\n        return n\n    return linear_time_7(n-1) + 1",
    "complexity": "O(n)"
}