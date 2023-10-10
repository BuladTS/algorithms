import collections
from functools import lru_cache


class Solution:
    @staticmethod
    def pathsWithMaxScore(board: list[str]) -> list[int]:

        length, mod = len(board), 10 ** 9 + 7

        @lru_cache(None)
        def dfs(i, j):
            if i >= length or j >= length or board[i][j] == 'X':
                return float('-inf'), 0

            if i == length - 1 and j == length - 1:
                return 0, 1

            op1 = dfs(i + 1, j)
            op2 = dfs(i, j + 1)
            op3 = dfs(i + 1, j + 1)

            score = int(board[i][j]) if board[i][j] != 'E' else 0

            count, prev_score = 0, max(op1[0], op2[0], op3[0])

            if op1[0] == prev_score:
                count += op1[1]
            if op2[0] == prev_score:
                count += op2[1]
            if op3[0] == prev_score:
                count += op3[1]

            return score + prev_score, count % mod

        res = dfs(0, 0)
        return [max(res[0], 0), res[1]]

        # length = len(board)
        # res = collections.defaultdict(lambda: 0)
        #
        # moves = [(-1, -1), (-1, 0), (0, -1)]
        #
        # def helper(row, col, score):
        #     nonlocal res, length
        #     if board[row][col] == 'E':
        #         res[score] += 1
        #
        #     for m_i, m_j in moves:
        #         new_row, new_col = row + m_i, col + m_j
        #         if 0 <= new_row < length and 0 <= new_col < length and board[new_row][new_col] != 'X':
        #             if board[new_row][new_col] == 'E':
        #                 helper(new_row, new_col, score)
        #             else:
        #                 helper(new_row, new_col, score + int(board[new_row][new_col]))
        #
        # helper(length - 1, length - 1, 0)
        # if res.keys():
        #     max_score = max(res.keys())
        # else:
        #     return [0, 0]
        #
        # return [max_score, res[max_score]]


def main():
    print(Solution.pathsWithMaxScore(["E23", "2X2", "12S"]))
    print(Solution.pathsWithMaxScore(["E12", "1X1", "21S"]))
    print(Solution.pathsWithMaxScore(["E12", "XXX", "21S"]))


if __name__ == "__main__":
    main()

