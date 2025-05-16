{
    "code": "def exponential_time_16(weights, values, capacity):\n    n = len(weights)\n    \n    def knapsack(i, remaining_capacity):\n        if i == n or remaining_capacity == 0:\n            return 0\n        \n        # Skip item i\n        result = knapsack(i + 1, remaining_capacity)\n        \n        # Take item i if possible\n        if weights[i] <= remaining_capacity:\n            result = max(result, values[i] + knapsack(i + 1, remaining_capacity - weights[i]))\n        \n        return result\n    \n    return knapsack(0, capacity)",
    "complexity": "O(2^n)"
}