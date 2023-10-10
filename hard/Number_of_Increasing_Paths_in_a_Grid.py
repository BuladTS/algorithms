class Solution:
    @staticmethod
    def countPaths(grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        mod = 10 ** 9 + 7
        moves = [[0, -1], [0, 1], [1, 0], [-1, 0]]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            answer = 1

            for mi, mj in moves:
                prev_i, prev_j = i + mi, j + mj
                if 0 <= prev_i < m and 0 <= prev_j < n and grid[prev_i][prev_j] < grid[i][j]:
                    answer += dfs(prev_i, prev_j) % mod

            dp[i][j] = answer
            return answer
        # return sum(dfs(i, j) for i in range(m) for j in range(n))
        result = 0
        for i in range(m):
            for j in range(n):
                result += dfs(i, j)

        return result % mod

        # m, n = len(grid), len(grid[0])
        # count = 0
        #
        # def dfs(i, j):
        #     nonlocal count
        #     if i + 1 < m and grid[i][j] < grid[i + 1][j]:
        #         dfs(i + 1, j)
        #         count += 1
        #     if i - 1 >= 0 and grid[i][j] < grid[i - 1][j]:
        #         dfs(i - 1, j)
        #         count += 1
        #     if j + 1 < n and grid[i][j] < grid[i][j + 1]:
        #         dfs(i, j + 1)
        #         count += 1
        #     if j - 1 >= 0 and grid[i][j] < grid[i][j - 1]:
        #         dfs(i, j - 1)
        #         count += 1
        # for i in range(m):
        #     for j in range(n):
        #         dfs(i, j)
        #         count += 1
        # return count


if __name__ == "__main__":
    print(Solution.countPaths([[1, 1], [3, 4]]))
    print(Solution.countPaths([[1], [2]]))
