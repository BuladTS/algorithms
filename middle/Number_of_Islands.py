class Solution:
    @staticmethod
    def numIslands(grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        ways = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(i, j):
            grid[i][j] = '2'
            for m1, m2 in ways:
                new_i, new_j = i + m1, j + m2
                if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] == '1':
                    dfs(new_i, new_j)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count


def main():
    print(Solution.numIslands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))

    print(Solution.numIslands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]))


if __name__ == "__main__":
    main()
