{
    "code": "def linear_time_22(decimal_number):\n    if decimal_number == 0:\n        return '0'\n    # Convert to any base (here base 16 for hex)\n    digits = \"0123456789ABCDEF\"\n    result = \"\"\n    temp = abs(decimal_number)\n    while temp > 0:\n        result = digits[temp % 16] + result\n        temp //= 16\n    return ('-' if decimal_number < 0 else '') + result",
    "complexity": "O(n)"
}