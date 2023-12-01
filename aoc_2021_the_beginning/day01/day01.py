from typing import List

def count_increases(depths: List[int]) -> int:
    return sum([1 for x, y in zip(depths, depths[1:]) if x < y ])

def count_increases_per_windows(depths: List[int]) -> int:
    measurements = [(x + y + z) for x, y, z in zip(depths, depths[1:], depths[2:])]
    return count_increases(measurements)





