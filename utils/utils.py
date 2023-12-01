from typing import List

def read_file(file_path: str) -> List[str]:
    with open(file_path, "r") as reader:
        lines = reader.readlines()
    return [line.strip() for line in lines]

def parse_lines(lines: List[str]) -> List[List[int]]:
    lines = [list(line) for line in lines]
    lines = [[int(digit) for digit in line] for line in lines]
    return lines