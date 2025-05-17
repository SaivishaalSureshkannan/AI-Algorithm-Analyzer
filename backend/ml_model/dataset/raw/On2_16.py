{
    "code": "def quadratic_time_16(n):\n    dp = [0] * (n + 1)\n    dp[0] = 1\n    \n    for i in range(1, n + 1):\n        # Modified inner loop to run up to i instead of constant 7\n        # This makes the time complexity O(n²)\n        for j in range(1, i + 1):\n            if i - j >= 0:\n                dp[i] += dp[i - j]\n    \n    return dp[n]",
    "complexity": "O(n^2)"
}