import aoc_2021.day01.test_day01 as day1
import aoc_2021.day02.test_day02 as day2
import aoc_2021.day03.test_day03 as day3
import aoc_2021.day04.test_day04 as day4


def test_day01():
    #part one
    day1.test_count_increases_short_one()
    day1.test_count_increases_short_two()
    day1.test_count_increases_short_three()
    day1.test_count_increases_long()

    #part two
    day1.test_count_increases_per_windows_short_one()
    day1.test_count_increases_per_windows_short_two()
    day1.test_count_increases_per_windows_short_three()
    day1.test_count_increases_per_windows_long()

def test_day02():
    day2.test_calculate_submarine_position_short()
    day2.test_calculate_submarine_position_long()

def test_day03():
    #day3.test_calculate_power_consumption_short()
    #day3.test_calculate_power_consumption_long()
    day3.test_calculate_life_support_rating_short()
    day3.test_calculate_life_support_rating_long()

def main():
    #test_day01()
    #test_day02()
    #test_day03()
    day4.test_board_functions()



if __name__ == '__main__':
    main()
