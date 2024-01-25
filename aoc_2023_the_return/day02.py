from aocd import get_data

def test_validity(game, cubes_in_the_bag):
    print(game)
    print(cubes_in_the_bag)
    id, rolls = game
    validities = []
    for roll in rolls:
        roll = list(map(str.strip, roll.split(",")))
        print("roll", roll)
        validities += [False if cubes_in_the_bag[cubes.split()[1].strip()] < int(cubes.split()[0].strip()) else True for cubes in roll]
        print(validities)
    if False not in validities:
        return int(id)
    return 0

def parse_input(data):
    def _str2tuple(line):
        line_split = line.split(":")
        return (line_split[0].split()[1].strip(), list(map(str.strip,line_split[1].split(";"))))
    
    lines = data.splitlines()
    games = [_str2tuple(line) for line in lines]
    return games

def part1(data, cubes_in_the_bag = {}):
    games = parse_input(data)
    valid_games = [test_validity(game, cubes_in_the_bag) for game in games]
    res = sum(valid_games)
    return res

def part2(data):
    games = parse_input(data)
    print(games)
    min_cubes_in_bag = dict()



puzzle = get_data(day=2, year=2023)

example1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

#print(part1(example1, {"red": 12, "green": 13, "blue": 14}) == 8)
#print(part1(puzzle,  {"red": 12, "green": 13, "blue": 14}))

#print(part2(example1, {"red": 12, "green": 13, "blue": 14}) == 2286)
#print(part2(puzzle,  {"red": 12, "green": 13, "blue": 14}))