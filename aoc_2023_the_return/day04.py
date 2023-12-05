from aocd import get_data, submit

def split_numbers(card_line):
    return (card_line.split("|")[0].split(), card_line.split("|")[1].split())

def list_intersection(list1, list2):
    return [i for i in list2 if i in list1]

def calc_card_score(nrs_count):
    if nrs_count == 0:
        return 0
    res = 2**(nrs_count - 1)
    return res

def parse_input(data):
    lines = data.splitlines()
    cards = [line.split(":")[1] for line in lines]
    numbers = [split_numbers(line) for line in cards]
    return numbers, len(cards)

def part1(data):
    numbers, _ = parse_input(data)
    winning_nrs_counts = [len(list_intersection(card_nrs, my_nrs)) for card_nrs, my_nrs in numbers]
    res = sum([calc_card_score(count) for count in winning_nrs_counts])
    return res

def part2(data):
    numbers, nr_of_cards = parse_input(data)
    winning_nrs_counts = [len(list_intersection(card_nrs, my_nrs)) for card_nrs, my_nrs in numbers]
    card_counts = dict(zip(range(1, nr_of_cards+1), [1]*nr_of_cards))
    for i, winning_nrs_count in enumerate(winning_nrs_counts):
        current_card_count = card_counts[i+1]
        for j in range(winning_nrs_count):
            card_counts[i+j+2] += current_card_count
    res = sum(card_counts.values())
    return res

example1 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
puzzle = get_data(day=4, year=2023)

print("Total number of points in the given example is 13: ", part1(example1)==13)
print("Total number of points in the puzzle:", part1(puzzle))

print("Total number of scratchcards in the given example is 30: ", part2(example1)==30)
print("Total number of scratchcards in the puzzle:", part2(puzzle))