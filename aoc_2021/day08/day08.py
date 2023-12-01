from typing import List

UNIQUE_LENGTHS = {"1": 2, "4": 4, "7": 3, "8": 7}

# The following dictionary contains: 
# (#symbols, # of common symbols with digit 1, # of common symbols with digit 1): digit
DECODE = {
    (6, 2, 3): "0",
    (2, 2, 2): "1",
    (5, 1, 2): "2",
    (5, 2, 3): "3",
    (4, 2, 4): "4",
    (5, 1, 3): "5",
    (6, 1, 3): "6",
    (3, 2, 2): "7",
    (7, 2, 4): "8",
    (6, 2, 4): "9",
}

with open("./inputs/day08.txt", "r") as reader:
    inputs, outputs = [], []
    for line in reader:
        input, output = line.strip().split("|")
        inputs += [input.strip()]
        outputs += [output.strip()]

# PART ONE
def count_unique_outputs(outputs: List[str]) -> int:
    unique_outputs_counter = 0

    for output in outputs:
        for signal in output.split(' '):
            if len(signal) in UNIQUE_LENGTHS.values():
                unique_outputs_counter += 1

    return unique_outputs_counter

counts = count_unique_outputs(outputs)

print(f"Digits 1, 4, 7 and 8 appear {counts} times in the output values.")


# PART TWO
# adapted from https://github.com/salt-die/Advent-of-Code/blob/master/2021/day_08.py
# did not manage on my own this time but I found this beautiful solution and I wanted to save it
def decode_signal(inputs: List[str], outputs: List[str]) -> List[str]:
    decoded_outputs = []
    for i in range(len(inputs)):
        input = inputs[i].split(' ')
        output = outputs[i].split(' ')
        one, _, four, *_ = sorted(input, key=len)
        one = set(one)
        four = set(four)

        decoded_outputs += ["".join(
            DECODE[
                len(digit),
                len(one.intersection(digit)),
                len(four.intersection(digit)),
            ]
            for digit in output
        )]

    return decoded_outputs


def sum_outputs(inputs: List[str], outputs: List[str]) -> int:
    decoded_outputs = decode_signal(inputs, outputs)
    return sum([int(i) for i in decoded_outputs])

sum_all = sum_outputs(inputs, outputs)
print(f"Sum of all output values is {sum_all}")

