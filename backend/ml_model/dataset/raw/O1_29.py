{
    "code": "def constant_time_29(matrix3x3):\n    # Calculate determinant of 3x3 matrix\n    a, b, c = matrix3x3[0]\n    d, e, f = matrix3x3[1]\n    g, h, i = matrix3x3[2]\n    \n    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)\n    return det",
    "complexity": "O(1)"
}