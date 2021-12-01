import utils
import day01.day01 as day01

TEST_ONE = ["199", "200", "208", "210"]
TEST_TWO = ["199", "200", "208", "210", "34", "35"]
TEST_THREE = ["199", "200", "208", "210", "200", "240", "269", "260", "263"]

def test_count_increases_short_one():
    depths = [int(i) for i in TEST_ONE]
    print(day01.count_increases(depths))

def test_count_increases_short_two():
    depths = [int(i) for i in TEST_TWO]
    print(day01.count_increases(depths))

def test_count_increases_short_three():
    depths = [int(i) for i in TEST_THREE]
    print(day01.count_increases(depths))

def test_count_increases_long():
    depths = [int(i) for i in utils.read_file("./inputs/day01.txt")]
    print(day01.count_increases(depths))

def test_count_increases_per_windows_short_one():
    depths = [int(i) for i in TEST_ONE]
    print(day01.count_increases_per_windows(depths))

def test_count_increases_per_windows_short_two():
    depths = [int(i) for i in TEST_TWO]
    print(day01.count_increases_per_windows(depths))

def test_count_increases_per_windows_short_three():
    depths = [int(i) for i in TEST_THREE]
    print(day01.count_increases_per_windows(depths))

def test_count_increases_per_windows_long():
    depths = [int(i) for i in utils.read_file("./inputs/day01.txt")]
    print(day01.count_increases_per_windows(depths))
