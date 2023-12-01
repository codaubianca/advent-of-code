from typing import List, Tuple

def count_one_bit(diagnostic_report: List[str]) -> List[int]:
    one_bit = [0 for i in range(len(diagnostic_report[0]))]
    for diagnostic in diagnostic_report:
        for i in range(len(diagnostic)):
            if diagnostic[i] == '1':
                one_bit[i] += 1
    return one_bit

def calculate_gamma_and_epsilon_rate(diagnostic_report: List[str]) -> Tuple[int]:
    one_bit = count_one_bit(diagnostic_report)
    length_report = len(diagnostic_report)
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(len(one_bit)):
        if one_bit[i] < length_report - one_bit[i]:
            epsilon_rate += '1'
            gamma_rate += '0'
        else:
            epsilon_rate += '0'
            gamma_rate += '1'
    return int(epsilon_rate, 2), int(gamma_rate,2)

def calculate_power_consumption(diagnostic_report: List[str]):
    epsilon_rate, gamma_rate = calculate_gamma_and_epsilon_rate(diagnostic_report)
    return epsilon_rate * gamma_rate

def calculate_rating(diagnostic_report: List[str], most_common: str, least_common: str) -> str:
     idx = 0
     while len(diagnostic_report) > 1:
        le = len(diagnostic_report)
        one_bit = count_one_bit(diagnostic_report)
        if one_bit[idx] >= le - one_bit[idx]:
            diagnostic_report = [i for i in diagnostic_report if i[idx] == most_common]
        else:
            diagnostic_report = [i for i in diagnostic_report if i[idx] == least_common]
        idx += 1
     return diagnostic_report[0]

def calculate_life_support_rating(diagnostic_report: List[str]) -> int:
    o2 = calculate_rating(diagnostic_report, '1', '0')
    co2 = calculate_rating(diagnostic_report, '0', '1')
    return int(o2, 2) * int(co2, 2)


