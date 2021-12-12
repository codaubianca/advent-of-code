from typing import List

def read_file(file_path: str) -> List[str]:
    with open(file_path, "r") as reader:
        lines = reader.readlines()
    return [line.strip() for line in lines]
