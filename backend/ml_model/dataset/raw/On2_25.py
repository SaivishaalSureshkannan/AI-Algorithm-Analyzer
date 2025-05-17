{
    "code": "def quadratic_time_25(matrix):\n    # Rotate image by 90 degrees clockwise in-place\n    n = len(matrix)\n    # Transpose the matrix\n    for i in range(n):\n        for j in range(i, n):\n            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]\n    # Reverse each row\n    for i in range(n):\n        for j in range(n // 2):\n            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]\n    return matrix",
    "complexity": "O(n^2)"
}