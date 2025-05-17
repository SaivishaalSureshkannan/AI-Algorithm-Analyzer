{
    "code": "def linear_time_26(nums):\n    # Dutch national flag algorithm (3-way partitioning)\n    # Sorts an array of 0s, 1s, and 2s in a single pass\n    low, mid, high = 0, 0, len(nums) - 1\n    while mid <= high:\n        if nums[mid] == 0:\n            nums[low], nums[mid] = nums[mid], nums[low]\n            low += 1\n            mid += 1\n        elif nums[mid] == 1:\n            mid += 1\n        else:  # nums[mid] == 2\n            nums[mid], nums[high] = nums[high], nums[mid]\n            high -= 1\n    return nums",
    "complexity": "O(n)"
}