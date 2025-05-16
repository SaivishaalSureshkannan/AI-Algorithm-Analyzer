{
    "code": "def quadratic_time_5(n):\n    count = 0\n    i = 0\n    while i < n:\n        j = 0\n        while j < n:\n            count += 1\n            j += 1\n        i += 1\n    return count",
    "complexity": "O(n^2)"
}