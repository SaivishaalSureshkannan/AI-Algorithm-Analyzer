{
    "code": "def exponential_time_3(s, memo={}):\n    if s in memo:\n        return memo[s]\n    if len(s) <= 1:\n        return [s]\n    result = []\n    for i in range(len(s)):\n        char = s[i]\n        remaining = s[:i] + s[i+1:]\n        for p in exponential_time_3(remaining, memo):\n            result.append(char + p)\n    memo[s] = result\n    return result",
    "complexity": "O(2^n)"
}