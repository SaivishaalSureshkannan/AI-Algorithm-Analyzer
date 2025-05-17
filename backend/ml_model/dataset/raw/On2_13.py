{
    "code": "def quadratic_time_13(strings):\n    n = len(strings)\n    result = []\n    for i in range(n):\n        for j in range(n):\n            if i != j and strings[i] == strings[j]:\n                result.append((strings[i], strings[j]))\n    return result",
    "complexity": "O(n^2)"
}