{
    "code": "def exponential_time_5(n):\n    if n <= 0:\n        return 1\n    return exponential_time_5(n-1) + exponential_time_5(n-1)",
    "complexity": "O(2^n)"
}