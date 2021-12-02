import utils
import day02.day02 as day02

TEST = [("forward", 5), ("down", 5), ("forward", 8), ("up", 3), ("down", 8), ("forward", 2)]

def test_calculate_submarine_position_short():
    horizontal, depth = day02.calculate_submarine_position(TEST)
    print(f"Horizontal position: {horizontal}")
    print(f"Depth:{depth}")
    print(f"Multiplied: {depth*horizontal}")

def test_calculate_submarine_position_long():
    moves = [(move, int(units)) for move, units in [line.split() for line in utils.read_file('./inputs/day02.txt')]]
    horizontal, depth = day02.calculate_submarine_position(moves)
    print(f"Horizontal position: {horizontal}")
    print(f"Depth:{depth}")
    print(f"Multiplied: {depth*horizontal}")