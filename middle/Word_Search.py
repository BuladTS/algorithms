import collections


class Solution:
    @staticmethod
    def exist(board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col, visited: set, index):
            if index == len(word) - 1:
                return True
            visited.add((row, col))
            for m_i, m_j in moves:
                new_row = m_i + row
                new_col = m_j + col
                if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] == word[index + 1] \
                        and (new_row, new_col) not in visited:
                    if dfs(new_row, new_col, visited, index + 1):
                        return True
            visited.remove((row, col))
            return False
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, set(), 0):
                        return True
        return False


def main():
    print(Solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
    print(Solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
    print(Solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))



if __name__ == "__main__":
    main()
