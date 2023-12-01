from typing import List

class Board:
    def __init__(self, board: List[List[int]]) -> None:
        self.board = board
        self.height = len(self.board)
        self.width = len(self.board[0])
        self.marked_board = [[False for _ in range(self.width)] for _ in range(self.height)]

    def mark_number(self, number: int) -> None:
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == number:
                    #print(f"Found number{number}")
                    self.marked_board[i][j] = True
    
    def check_win(self) -> bool:
        return any([all(row) for row in self.marked_board]) or \
                any([all(column) for column in [[row[i] for row in self.marked_board] for i in range(self.width)]])

    def sum_unmarked(self) -> int:
        sum = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.marked_board[i][j] == False:
                    sum += self.board[i][j]
        return sum

