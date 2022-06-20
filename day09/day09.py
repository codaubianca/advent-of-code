from audioop import mul
from lib2to3.pgen2.literals import simple_escapes
from typing import List, Tuple

TEST = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678"

def read_file(file_path: str) -> List[str]:
    with open(file_path, "r") as reader:
        lines = reader.readlines()
    return [line.strip() for line in lines]

def parse_lines(lines: List[str]) -> List[List[int]]:
    lines = [list(line) for line in lines]
    lines = [[int(digit) for digit in line] for line in lines]
    return lines

def _add_padding(lines: List[List[int]]) -> List[List[int]]:
    limit = len(lines[0]) + 2
    pad_line = [9] * limit
    lines = [[9] + line + [9] for line in lines]
    lines = [pad_line] + lines + [pad_line]
    return lines

def _find_low_points(lines: List[List[int]]):
    low_points = []
    padded_lines = _add_padding(lines)
    row_limit = len(padded_lines) - 1
    column_limit = len(padded_lines[0]) - 1

    for i in range(1, row_limit):
        #print("new line")
        for j in range(1, column_limit):
            minima = min([padded_lines[i-1][j], padded_lines[i+1][j], padded_lines[i][j-1], padded_lines[i][j+1]])
            #print(f"elem: {padded_lines[i][j]}, minim: {minima}")
            if padded_lines[i][j] < minima:
                low_points += [(i-1, j-1)]
                print(f"i: {i}, j: {j}, elem: {padded_lines[i][j]}")

    return low_points

def calculate_risk(lines: List[List[int]]) -> int:
    low_points = _find_low_points(lines)
    return sum([lines[i][j] + 1 for (i, j) in low_points])

def _get_size_of_basin(padded_lines: List[List[int]], low_point: Tuple[int, int], basin: List[Tuple[int,int]]):

    i, j = low_point

    if (i, j) in basin:
        return 0

    if padded_lines[i][j] == 9:
        return 0

    basin += [low_point]

    return 1 + _get_size_of_basin(padded_lines, (i - 1, j), basin) + _get_size_of_basin(padded_lines, (i + 1, j), basin) \
        + _get_size_of_basin(padded_lines, (i, j - 1), basin) + _get_size_of_basin(padded_lines, (i, j + 1), basin)
    
def multiply_all_basin_sizes(lines: List[List[int]]):
    padded_lines = _add_padding(lines)
    low_points = _find_low_points(lines)
    sizes = []
    for i,j in low_points:
        size_of_basin = _get_size_of_basin(padded_lines, (i+1, j+1), [])
        print(size_of_basin)
        sizes += [size_of_basin]
    
    sizes = sorted(sizes, reverse=True)
       
    return sizes[0] * sizes[1] * sizes[2]

def test_part_one():
    lines = parse_lines(TEST.split('\n'))
    assert calculate_risk(lines) == 15


def test_part_two():
    lines = parse_lines(TEST.split('\n'))
    assert multiply_all_basin_sizes(lines) == 1134


lines = read_file("inputs/day09.txt")
lines = parse_lines(lines)

# PART ONE
total_risk = calculate_risk(lines)
print(f"The sum of the risk levels of all points is {total_risk}.")

# PART TWO
product = multiply_all_basin_sizes(lines)
print(f"Product of sizes of three largest basins: {product}.")

