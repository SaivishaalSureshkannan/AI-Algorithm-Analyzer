{
    "code": "def constant_time_15(a, b):\n    for _ in range(50):\n        a = (a + b) % 100\n        b = (a * b) % 100\n    return a ^ b",
    "complexity": "O(1)"
}