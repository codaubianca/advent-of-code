from day04.day04 import Board

def test_board_functions():
    with open("./inputs/day04.txt", "r") as reader:
        sections = reader.read().strip().split('\n\n')

    numbers = [int(num) for num in sections[0].split(',')]
    boards = [board.split('\n') for board in sections[1:]]
    boards = [[[int(num) for num in line.split()] for line in board]for board in boards]
    boards = [Board(board) for board in boards]

    winners = []
    for number in numbers:
        for i in range(len(boards) - 1, -1, -1):
            board = boards[i]
            board.mark_number(number)
            if board.check_win() == True:
                sum_unmarked = board.sum_unmarked()
                final_score = sum_unmarked * number
                print(f"Board won with sum of unmarked = {sum_unmarked}" +
                f" when number = {number} and final score = {final_score}")
                winners.append(final_score)
                boards.remove(board)
            if number == 13:
                    print(f"Number 13: second board third column marked: {[row[2] for row in board.marked_board]}")
            if number == 16:
                    print(f"Number 16: second board third column marked: {[row[2] for row in board.marked_board]}")
    print(winners.pop())
    