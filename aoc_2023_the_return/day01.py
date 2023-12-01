from aocd import get_data, submit
import re

def get_numbers(line):
    numbers = re.sub("[^0-9]", "", line)
    calibration = int(numbers[0] + numbers[-1])
    return calibration

def part1(data):
    res = sum([get_numbers(line) for line in data.splitlines()])
    return res



def get_numbers2(line):
    numbers = "0123456789"
    word2number = {'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    }
    res = []
    j=0
    for i in range(len(line)):
        if line[i] in numbers:
            res.append(int(line[i]))
        for word in word2number.keys():
            if word in line[j:i+1]:
                res.append(word2number[word])
                j=i+1
    return res

def part2(data):
    res = 0
    for line in data.splitlines():
        numbers = get_numbers2(line)
        if len(numbers) > 1:
            calibration = numbers[0]*10 + numbers[-1]
        else:
            calibration = numbers[0]
        print(line, calibration)
        res += calibration
    return res

def replace_numbers(str):
    numbers = [
        ("one", "one1one"),
        ("two", "two2two"),
        ("three", "three3three"),
        ("four", "four4four"),
        ("five", "five5five"),
        ("six", "six6six"),
        ("seven", "seven7seven"),
        ("eight", "eight8eight"),
        ("nine", "nine9nine"),
    ]
    for r in numbers:
        str = str.replace(*r)

    return str

def part2_(data):
    input = [replace_numbers(line) for line in data.splitlines()]
    res = sum([get_numbers(line) for line in input])
    return res

example1 =   """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
print(part1(example1)==142)      

puzzle = get_data(day=1, year=2023)
#print(part1(puzzle))

example2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
print(part2_(example2) == 281)
print(part2_(puzzle))

