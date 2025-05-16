{
    "code": "def quadratic_time_19(nums):\n    n = len(nums)\n    dp = [[0] * n for _ in range(n)]\n    \n    # dp[i][j] represents the max score for subarray nums[i:j+1]\n    for length in range(1, n + 1):\n        for i in range(n - length + 1):\n            j = i + length - 1\n            for k in range(i, j + 1):\n                left = dp[i][k - 1] if k > i else 0\n                right = dp[k + 1][j] if k < j else 0\n                dp[i][j] = max(dp[i][j], left + nums[k] + right)\n    \n    return dp[0][n - 1]",
    "complexity": "O(n^2)"
}