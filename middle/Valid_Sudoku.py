import collections


class Solution:
    @staticmethod
    def isValidSudoku(board: list[list[str]]) -> bool:
        for sec_row in range(3):
            for sec_col in range(3):
                section = set()
                for row in range(3 * sec_row, 3 * (sec_row + 1)):
                    for col in range(3 * sec_col, 3 * (sec_col + 1)):
                        if board[row][col] in section:
                            return False
                        if board[row][col] != '.':
                            section.add(board[row][col])

        hash_map = {'0x': set(), '1x': set(), '2x': set(), '3x': set(), '4x': set(), '5x': set(),
                    '6x': set(), '7x': set(), '8x': set(), '0y': set(), '1y': set(), '2y': set(),
                    '3y': set(), '4y': set(), '5y': set(), '6y': set(), '7y': set(), '8y': set()}
        for row in range(9):
            for col in range(9):
                if board[row][col] in hash_map[f'{row}x'] or board[row][col] in hash_map[f'{col}y']:
                    return False
                if board[row][col] != '.':
                    hash_map[f'{row}x'].add(board[row][col])
                    hash_map[f'{col}y'].add(board[row][col])
        return True


def main():
    print(Solution.isValidSudoku(
        [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))
    print(Solution.isValidSudoku(
        [["8", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    ))


if __name__ == "__main__":
    main()
