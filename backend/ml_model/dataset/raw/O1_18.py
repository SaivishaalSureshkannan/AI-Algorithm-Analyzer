{
    "code": "def constant_time_18(nums):\n    # Get stats from fixed-size collection\n    if not nums:\n        return None\n    total = sum(nums)\n    minimum = min(nums)\n    maximum = max(nums)\n    return {'avg': total/len(nums), 'min': minimum, 'max': maximum}",
    "complexity": "O(1)"
}