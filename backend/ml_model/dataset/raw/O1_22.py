{
    "code": "def constant_time_22(settings):\n    default_config = {'mode': 'standard', 'level': 1, 'sound': True, 'theme': 'dark'}\n    # Update defaults with provided settings\n    for key in settings:\n        if key in default_config:\n            default_config[key] = settings[key]\n    return default_config",
    "complexity": "O(1)"
}