{
    "code": "def exponential_time(n):\n    if n <= 1:\n        return n\n    return exponential_time(n-1) + exponential_time(n-2)",
    "complexity": "O(2^n)"
} 