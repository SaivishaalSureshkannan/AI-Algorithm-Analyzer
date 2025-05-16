{
    "code": "def quadratic_time_16(n):\n    dp = [0] * (n + 1)\n    dp[0] = 1\n    \n    for i in range(1, n + 1):\n        for j in range(1, min(i + 1, 7)):\n            dp[i] += dp[i - j]\n    \n    return dp[n]",
    "complexity": "O(n^2)"
}