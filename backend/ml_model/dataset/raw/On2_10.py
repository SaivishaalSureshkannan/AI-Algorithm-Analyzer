{
    "code": "def quadratic_time_10(n):\n    # Triangle numbers pattern\n    result = 0\n    for i in range(1, n+1):\n        for j in range(1, i+1):\n            result += 1\n    return result",
    "complexity": "O(n^2)"
}