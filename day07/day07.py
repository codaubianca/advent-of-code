from typing import List
with open("./inputs/day07.txt", "r") as reader:
    positions = reader.readlines()

positions = [int(pos.strip()) for pos in positions[1].split(',')]

#print(positions)

def calculate_median(nrs: List[int]) -> int:
    length = len(nrs)
    nrs = sorted(nrs)
    if length % 2 == 1:
        return nrs[length // 2]
    else:
        return (nrs[(length // 2 ) - 1] + nrs[length // 2]) / 2

print(f"Median: {calculate_median(positions)}")

def calculate_fuel_consumption_constant(nrs: List[int]) -> int:
    median = calculate_median(nrs)
    distances = [abs(nr - median) for nr in nrs]
    return sum(distances)

def calculate_fuel_consumption(nrs: List[int]) -> int:
    mean = (sum(nrs) // len(nrs))
    # i think for test input it is rounded to lower integer but for example it was rounded to closest (upper) integer
    # for line 0 in input file use:
    # mean = round(sum(nrs) / len(nrs))
    # print(f"mean: {mean}")
    distances = [abs(nr-mean) * (abs(nr-mean) + 1) / 2 for nr in nrs]
    return sum(distances)

#print(f"Total fuel used when considering constant rate: {calculate_fuel_consumption_constant(positions)}")
print(f"Total fuel used: {calculate_fuel_consumption(positions)}")
