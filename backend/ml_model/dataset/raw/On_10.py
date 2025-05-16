{
    "code": "def linear_time_10(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a + b\n    return a",
    "complexity": "O(n)"
}