{
    "code": "def exponential_time_1(n):\n    if n <= 1:\n        return n\n    return exponential_time_1(n-1) + exponential_time_1(n-2)",
    "complexity": "O(2^n)"
}