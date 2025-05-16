{
    "code": "def quadratic_time_1(n):\n    result = 0\n    for i in range(n):\n        for j in range(n):\n            result += i * j\n    return result",
    "complexity": "O(n^2)"
}