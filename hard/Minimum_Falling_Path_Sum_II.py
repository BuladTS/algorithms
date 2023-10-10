class Solution:
    @staticmethod
    def minFallingPathSum(grid: list[list[int]]) -> int:
        n = len(grid)
        for i in range(1, n):
            temp = sorted(grid[i - 1])
            for j in range(n):
                if grid[i - 1][j] == temp[0]:
                    grid[i][j] += temp[1]
                else:
                    grid[i][j] += temp[0]
        return min(grid[-1])
        # dp = {}
        # n = len(grid)
        # for i in range(n):
        #     dp[(n - 1, i)] = grid[n - 1][i]
        #
        # def helper(index):
        #     for i in range(n):
        #         min_value = float('inf')
        #         for j in range(n):
        #             if i != j:
        #                 min_value = min(min_value, dp[(index + 1, j)])
        #         dp[(index, i)] = grid[index][i] + min_value
        # for i in range(n - 2, -1, -1):
        #     helper(i)
        # min_res = float('inf')
        # for i in range(n):
        #     min_res = min(min_res, dp[(0, i)])
        # return min_res


def main():
    print(Solution.minFallingPathSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(Solution.minFallingPathSum([[7]]))


if __name__ == '__main__':
    main()
