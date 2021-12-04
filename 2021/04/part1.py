import os

from typing import List, Sequence, TextIO, Tuple


class BingoBoard:
    def __init__(self, board: Sequence[Sequence[int]]) -> None:
        # Assume board is 5x5
        self._array = board
        self._marked = [[False for _ in range(5)] for _ in range(5)]
        self._numbers = {self._array[i][j]: (i, j) for i in range(5) for j in range(5)}

    def mark_number(self, number: int) -> None:
        if number in self._numbers:
            i, j = self._numbers[number]
            self._marked[i][j] = True

    def check_for_winner(self) -> Tuple[bool, int]:
        # Returns win state and sum of winning row, col, diag
        for i in range(5):
            win = self.check_for_winning_row(i)
            if win:
                return True, self.get_board_value()
            win = self.check_for_winning_col(i)
            if win:
                return True, self.get_board_value()

        # win, val = self.check_for_winning_diag1()
        # if win:
        #     return win, val
        # win, val = self.check_for_winning_diag2()
        # if win:
        #     return win, val
        return False, 0

    def check_for_winning_row(self, i: int) -> bool:
        for j in range(5):
            if not self._marked[i][j]:
                return False
        return True

    def check_for_winning_col(self, j: int) -> bool:
        for i in range(5):
            if not self._marked[i][j]:
                return False
        return True

    def check_for_winning_diag1(self) -> bool:
        # Top left to bot right
        for i in range(5):
            if not self._marked[i][i]:
                return False
        return True

    def check_for_winning_diag2(self) -> bool:
        # Bot left to top right
        for i in range(5):
            if not self._marked[4 - i][i]:
                return False
        return True

    def get_board_value(self) -> int:
        return sum(
            [
                self._array[i][j]
                for i in range(5)
                for j in range(5)
                if not self._marked[i][j]
            ]
        )

    def __repr__(self) -> str:
        mystr = ""
        for i in range(5):
            for j in range(5):
                if self._marked[i][j]:
                    mystr += "*"
                else:
                    mystr += " "
                mystr += f"{self._array[i][j]:2d}"
                if j != 4:
                    mystr += " "
            mystr += "\n"
        return mystr


def parse_input(f: TextIO) -> Tuple[List[int], List[BingoBoard]]:
    lines = [x for x in f]
    numbers = [int(x) for x in lines[0].strip().split(",")]
    boards = []
    for i in range(2, len(lines), 6):
        boards.append(
            BingoBoard([[int(x) for x in lines[j].split()] for j in range(i, i + 5, 1)])
        )
    return numbers, boards


cur_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{cur_dir}/input") as f:
    numbers, boards = parse_input(f)

full_break = False
for number in numbers:
    print(f"Called number: {number}")
    for index, board in enumerate(boards):
        board.mark_number(number)
        print(f"Updated board {index}: \n {board}")
        win, val = board.check_for_winner()
        full_break = win

        if full_break:
            print(val)
            print(val * number)
            break

    if full_break:
        break
