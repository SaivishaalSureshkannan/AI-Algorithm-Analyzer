{
    "code": "def quadratic_time_21(heights):\n    # Calculate water trapped in an elevation map using brute force\n    if not heights:\n        return 0\n    n = len(heights)\n    total_water = 0\n    for i in range(n):\n        left_max = max(heights[:i+1]) if i > 0 else heights[0]\n        right_max = max(heights[i:]) if i < n-1 else heights[-1]\n        water_at_i = min(left_max, right_max) - heights[i]\n        if water_at_i > 0:\n            total_water += water_at_i\n    return total_water",
    "complexity": "O(n^2)"
}