import day01.test_day01 as day1

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

def main():
    test_day01()


if __name__ == '__main__':
    main()
