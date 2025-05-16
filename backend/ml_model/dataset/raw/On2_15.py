{
    "code": "def quadratic_time_15(s, p):\n    def is_match(s, p, i, j):\n        if j == len(p):\n            return i == len(s)\n        \n        first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')\n        \n        if j + 1 < len(p) and p[j + 1] == '*':\n            return is_match(s, p, i, j + 2) or (first_match and is_match(s, p, i + 1, j))\n        else:\n            return first_match and is_match(s, p, i + 1, j + 1)\n    \n    return is_match(s, p, 0, 0)",
    "complexity": "O(n^2)"
}