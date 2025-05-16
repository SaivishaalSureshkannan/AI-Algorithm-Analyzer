{
    "code": "def quadratic_time_3(matrix):\n    n = len(matrix)\n    result = 0\n    for i in range(n):\n        for j in range(n):\n            result += matrix[i][j]\n    return result",
    "complexity": "O(n^2)"
}