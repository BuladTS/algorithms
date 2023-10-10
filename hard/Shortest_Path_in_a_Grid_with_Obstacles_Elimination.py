class Solution:
    @staticmethod
    def shortestPath(grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        visited = set()

        def dfs(row, col, breaks, current_steps):
            if row == rows - 1 and col == cols - 1:
                return current_steps

            res = float('inf')
            for m_i, m_j in moves:
                new_row = row + m_i
                new_col = col + m_j
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col, breaks) not in visited:
                    visited.add((new_row, new_col, breaks))
                    if grid[new_row][new_col] == 0:
                        res = min(dfs(new_row, new_col, breaks, current_steps + 1), res)
                    elif breaks != 0:
                        res = min(dfs(new_row, new_col, breaks - 1, current_steps + 1), res)
                    visited.remove((new_row, new_col, breaks))

            return res

        ans = dfs(0, 0, k, 0)
        return ans if ans != float('inf') else -1


def main():
    print(Solution.shortestPath([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1))
    print(Solution.shortestPath([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1))


if __name__ == '__main__':
    main()
