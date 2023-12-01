from typing import List
from utils.utils import read_file, parse_lines

TEST = "11111\n19991\n19191\n19991\n11111\n"

def step(octopus_grid: List[List[int]]):
    n = len(octopus_grid)
    for i in range(n):
        for j in range(n):
            pass
            

def flash():
    pass

def count_flashes():
    pass

def test_step_simple():
    grid = parse_lines(TEST.split('\n'))

    