import day03.day03 as day03
import utils 

TEST = [
        "00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"
        ]

def test_calculate_power_consumption_short():
    epsilon, gamma = day03.calculate_gamma_and_epsilon_rate(TEST)
    print(f"Gamma rate: {gamma}")
    print(f"Epsilon rate: {epsilon}")
    print(f"Power consumption: {day03.calculate_power_consumption(TEST)}")
    
def test_calculate_power_consumption_long():
    diagnostic_report = utils.read_file("./inputs/day03.txt")
    epsilon, gamma = day03.calculate_gamma_and_epsilon_rate(diagnostic_report)
    print(f"Gamma rate: {gamma}")
    print(f"Epsilon rate: {epsilon}")
    print(f"Power consumption: {day03.calculate_power_consumption(diagnostic_report)}")

def test_calculate_life_support_rating_short():
    life_support = day03.calculate_life_support_rating(TEST)
    print(f"Life support rating: {life_support}")

def test_calculate_life_support_rating_long():
    diagnostic_report = utils.read_file("./inputs/day03.txt")
    life_support = day03.calculate_life_support_rating(diagnostic_report)
    print(f"Life support rating: {life_support}")
 