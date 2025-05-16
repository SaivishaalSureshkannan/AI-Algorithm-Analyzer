{
    "code": "def exponential_time_15(n):\n    def count_ways(n, memo=None):\n        if memo is None:\n            memo = {}\n        if n in memo:\n            return memo[n]\n        if n == 0:\n            return 1\n        if n < 0:\n            return 0\n        \n        memo[n] = count_ways(n - 1, memo) + count_ways(n - 2, memo) + count_ways(n - 3, memo)\n        return memo[n]\n    \n    return count_ways(n)",
    "complexity": "O(2^n)"
}