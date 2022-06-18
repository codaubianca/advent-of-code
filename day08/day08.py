unique_lengths = {"1": 2, "4": 4, "7": 3, "8": 7}

def count_unique_outputs(file_path: str) -> int:
    unique_outputs_counter = 0

    with open(file_path, "r") as reader:
        for line in reader:
            line_parts = line.strip().split("|")
            outputs = line_parts[1].split(" ")
            for output in outputs:
                if len(output) in unique_lengths.values():
                    unique_outputs_counter += 1

    return unique_outputs_counter

counts = count_unique_outputs("./inputs/day08.txt")

print(f"Digits 1, 4, 7 and 8 appear {counts} times in the output values.")

    
