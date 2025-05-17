{
    "code": "def quadratic_time_29(arr):\n    # Longest Increasing Subsequence\n    if not arr:\n        return 0\n    n = len(arr)\n    dp = [1] * n  # Length of LIS ending at index i\n    for i in range(1, n):\n        for j in range(i):\n            if arr[i] > arr[j]:\n                dp[i] = max(dp[i], dp[j] + 1)\n    return max(dp)",
    "complexity": "O(n^2)"
}