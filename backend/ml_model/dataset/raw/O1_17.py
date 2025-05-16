{
    "code": "def constant_time_17(array):\n    # Fisher-Yates shuffle for first 5 elements only\n    import random\n    n = min(5, len(array))\n    for i in range(n-1, 0, -1):\n        j = random.randint(0, i)\n        array[i], array[j] = array[j], array[i]\n    return array",
    "complexity": "O(1)"
}