from typing import List, Tuple

def calculate_submarine_position(moves: List[Tuple[str, int]]) -> Tuple[int, int]:
    horizontal_position, depth, aim = 0, 0, 0
    for i in range(len(moves)):
        move, units = moves[i]
        if move == 'forward':
            horizontal_position += units
            depth += aim * units
        elif move == 'down':
            aim += units
        elif move == 'up':
            aim -= units
    return (horizontal_position, depth)
