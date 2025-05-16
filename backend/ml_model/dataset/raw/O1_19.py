{
    "code": "def constant_time_19(grid):\n    # Check if 3x3 grid is valid for tic-tac-toe\n    # Check rows\n    for i in range(3):\n        if grid[i][0] == grid[i][1] == grid[i][2] != ' ':\n            return grid[i][0]\n    # Check columns\n    for i in range(3):\n        if grid[0][i] == grid[1][i] == grid[2][i] != ' ':\n            return grid[0][i]\n    # Check diagonals\n    if grid[0][0] == grid[1][1] == grid[2][2] != ' ':\n        return grid[0][0]\n    if grid[0][2] == grid[1][1] == grid[2][0] != ' ':\n        return grid[0][2]\n    return None",
    "complexity": "O(1)"
}