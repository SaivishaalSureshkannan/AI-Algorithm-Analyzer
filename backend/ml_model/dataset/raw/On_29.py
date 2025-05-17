{
    "code": "def linear_time_29(digit_string):\n    # Count ways to decode a digit string\n    if not digit_string or digit_string[0] == '0':\n        return 0\n    n = len(digit_string)\n    dp = [0] * (n+1)\n    dp[0] = 1\n    dp[1] = 1\n    for i in range(2, n+1):\n        # Check single digit\n        if digit_string[i-1] != '0':\n            dp[i] += dp[i-1]\n        # Check two digits\n        two_digit = int(digit_string[i-2:i])\n        if 10 <= two_digit <= 26:\n            dp[i] += dp[i-2]\n    return dp[n]",
    "complexity": "O(n)"
}