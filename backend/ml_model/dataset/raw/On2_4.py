{
    "code": "def quadratic_time_4(strings):\n    result = []\n    for s1 in strings:\n        for s2 in strings:\n            result.append(s1 + s2)\n    return result",
    "complexity": "O(n^2)"
}