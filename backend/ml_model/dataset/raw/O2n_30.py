{
    "code": "def exponential_time_30(nums, target):\n    # Subset sum: does any subset sum to target?\n    def dfs(index, current_sum):\n        if current_sum == target:\n            return True\n        if index == len(nums):\n            return False\n        # Include current number\n        if dfs(index + 1, current_sum + nums[index]):\n            return True\n        # Exclude current number\n        return dfs(index + 1, current_sum)\n    return dfs(0, 0)",
    "complexity": "O(2^n)"
}
