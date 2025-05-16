{
    "code": "def exponential_time_8(n):\n    def hanoi(n, source, auxiliary, target):\n        if n > 0:\n            # Move n-1 disks from source to auxiliary\n            hanoi(n-1, source, target, auxiliary)\n            # Move 1 disk from source to target\n            moves.append((source, target))\n            # Move n-1 disks from auxiliary to target\n            hanoi(n-1, auxiliary, source, target)\n    \n    moves = []\n    hanoi(n, 'A', 'B', 'C')\n    return moves",
    "complexity": "O(2^n)"
}