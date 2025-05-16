{
    "code": "def exponential_time_18(m, n):\n    def count_paths(i, j, memo=None):\n        if memo is None:\n            memo = {}\n        \n        if (i, j) in memo:\n            return memo[(i, j)]\n        \n        if i == m - 1 and j == n - 1:\n            return 1\n        if i >= m or j >= n:\n            return 0\n        \n        memo[(i, j)] = count_paths(i + 1, j, memo) + count_paths(i, j + 1, memo)\n        return memo[(i, j)]\n    \n    return count_paths(0, 0)",
    "complexity": "O(2^n)"
}