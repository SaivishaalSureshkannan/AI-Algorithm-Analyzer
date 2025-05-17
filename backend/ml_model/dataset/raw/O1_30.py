{
    "code": "def constant_time_30(date_string):\n    # Parse and validate simple date format YYYY-MM-DD\n    try:\n        year, month, day = map(int, date_string.split('-'))\n        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\n        days_in_month = [0, 31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]\n        if 1 <= month <= 12 and 1 <= day <= days_in_month[month]:\n            return True\n        return False\n    except:\n        return False",
    "complexity": "O(1)"
}