{
    "code": "def linear_time_30(commands):\n    # Robot movement simulation on a 2D grid\n    x, y = 0, 0\n    direction = 0  # 0: north, 1: east, 2: south, 3: west\n    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # dx, dy for each direction\n    for cmd in commands:\n        if cmd == 'G':\n            dx, dy = directions[direction]\n            x += dx\n            y += dy\n        elif cmd == 'L':\n            direction = (direction - 1) % 4\n        elif cmd == 'R':\n            direction = (direction + 1) % 4\n    return (x, y)",
    "complexity": "O(n)"
}