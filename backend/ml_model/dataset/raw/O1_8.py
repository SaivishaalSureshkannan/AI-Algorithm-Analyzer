{
    "code": "def constant_time_8(n):\n    result = 0\n    for _ in range(100):\n        result += n\n    return result",
    "complexity": "O(1)"
}