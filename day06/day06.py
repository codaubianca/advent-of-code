from typing import List
from collections import Counter

with open("./inputs/day06.txt", "r") as reader:
    fish_banks = reader.readlines()

fish_banks = [[int(days) for days in fish_bank.split(',')] for fish_bank in fish_banks]

fish_bank = fish_banks[1]
#print(fish_bank)
fish_days_counter = Counter(fish_bank)
for days in range(257):
    print(f"After {days} days: total fish count is {sum(units for _, units in fish_days_counter.items())}")
    new_fish = fish_days_counter[0]
    for remaining_days in range(0,9):
        fish_days_counter[remaining_days] = fish_days_counter[remaining_days + 1]
    fish_days_counter[6] += new_fish
    fish_days_counter[8] = new_fish






