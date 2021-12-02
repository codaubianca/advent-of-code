from typing import List, Tuple

def calculate_submarine_position(moves: List[Tuple[str, int]]) -> Tuple[int, int]:
    horizontal_position, depth = 0, 0
    for i in range(len(moves)):
        move, units = moves[i]
        if move == 'forward':
            horizontal_position += units
        elif move == 'down':
            depth += units
        elif move == 'up':
            depth -= units
    return (horizontal_position, depth)
