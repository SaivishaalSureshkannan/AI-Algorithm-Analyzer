{
    "code": "def quadratic_time_14(intervals):\n    if not intervals:\n        return []\n    \n    merged = []\n    intervals.sort(key=lambda x: x[0])\n    \n    for interval in intervals:\n        if not merged or merged[-1][1] < interval[0]:\n            merged.append(interval)\n        else:\n            merged[-1][1] = max(merged[-1][1], interval[1])\n    \n    return merged",
    "complexity": "O(n^2)"
}