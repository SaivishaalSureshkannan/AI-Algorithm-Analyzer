{
    "code": "def quadratic_time_8(words):\n    palindromes = []\n    for i in range(len(words)):\n        for j in range(i, len(words)):\n            combined = words[i] + words[j]\n            if combined == combined[::-1]:\n                palindromes.append(combined)\n    return palindromes",
    "complexity": "O(n^2)"
}