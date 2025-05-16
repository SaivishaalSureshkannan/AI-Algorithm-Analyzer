{
    "code": "def quadratic_time_13(strings):\n    groups = {}\n    for s in strings:\n        sorted_s = ''.join(sorted(s))\n        if sorted_s in groups:\n            groups[sorted_s].append(s)\n        else:\n            groups[sorted_s] = [s]\n    return list(groups.values())",
    "complexity": "O(n^2)"
}