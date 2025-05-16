{
    "code": "def quadratic_time_7(n):\n    result = []\n    for i in range(n):\n        row = []\n        for j in range(n):\n            row.append(i * j)\n        result.append(row)\n    return result",
    "complexity": "O(n^2)"
}