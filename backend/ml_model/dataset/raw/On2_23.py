{
    "code": "def quadratic_time_23(ratings):\n    n = len(ratings)\n    result = 0\n    for i in range(n):\n        for j in range(n):\n            if ratings[i] > ratings[j]:\n                result += 1\n    return result",
    "complexity": "O(n^2)"
}
