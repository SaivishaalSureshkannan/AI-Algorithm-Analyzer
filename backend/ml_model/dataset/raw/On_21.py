{
    "code": "def linear_time_21(logs, error_level):\n    errors = []\n    for log in logs:\n        if log.get('level') >= error_level:\n            timestamp = log.get('timestamp')\n            message = log.get('message')\n            errors.append(f\"[{timestamp}] {message}\")\n    return errors",
    "complexity": "O(n)"
}