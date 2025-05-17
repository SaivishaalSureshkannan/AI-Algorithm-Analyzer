{
    "code": "def linear_time_23(time_series):\n    # Exponential moving average\n    if not time_series:\n        return []\n    alpha = 0.1  # Smoothing factor\n    ema = [time_series[0]]\n    for i in range(1, len(time_series)):\n        ema.append(alpha * time_series[i] + (1 - alpha) * ema[-1])\n    return ema",
    "complexity": "O(n)"
}