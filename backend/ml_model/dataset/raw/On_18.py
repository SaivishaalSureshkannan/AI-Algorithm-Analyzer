{
    "code": "def linear_time_18(prices):\n    if not prices:\n        return 0\n    max_profit = 0\n    min_price = prices[0]\n    for price in prices:\n        min_price = min(min_price, price)\n        max_profit = max(max_profit, price - min_price)\n    return max_profit",
    "complexity": "O(n)"
}