from typing import List

ERROR_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

AUTOCOMPLETE_POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

MATCHING_BRACKETS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def read_data(file_path: str) -> List[str]:
    with open(file_path, "r") as reader:
        lines = reader.readlines()
    return [line.strip() for line in lines]

def find_error(line):
    stack = []
    for bracket in line:
        if bracket in MATCHING_BRACKETS.keys():
            stack.append(bracket)
        else:
            last = stack.pop()
            if MATCHING_BRACKETS[last] != bracket:
                return ERROR_SCORES[bracket]
    return 0

def calculate_total_error_score(data):
    total_error = 0
    for line in data:
        total_error += find_error(line)
    return total_error

def autocomplete(line):
    stack = []
    for bracket in line:
        if bracket in MATCHING_BRACKETS.keys():
            stack.append(bracket)
        else:
            if MATCHING_BRACKETS[stack[-1]] == bracket:
                stack.pop()
    return [MATCHING_BRACKETS[bracket] for bracket in stack]

def calculate_autocomplete_scores_per_line(data):
    scores = []
    for line in data:
        if find_error(line) != 0:
            continue
        missing_brackets = reversed(autocomplete(line))
        score = 0
        for bracket in missing_brackets:
            score = score * 5 + AUTOCOMPLETE_POINTS[bracket]
        scores.append(score)
    return scores

def get_middle_score(data):
    scores = calculate_autocomplete_scores_per_line(data)
    return sorted(scores)[len(scores) // 2]

def test_error_score_calculation():
    data = read_data("inputs/day10_short.txt")
    assert calculate_total_error_score(data) == 26397

def test_autocomplete_score_calculation():
    data = read_data("inputs/day10_short.txt")
    assert get_middle_score(data) == 288957

if __name__ == '__main__':
    # PART ONE
    data_one = read_data("inputs/day10.txt")
    error_score = calculate_total_error_score(data_one)
    print(f'Solution to part one: {error_score}')

    # PART TWO
    auto_score = get_middle_score(data_one)
    print(f'Solution to part two: {auto_score}')


