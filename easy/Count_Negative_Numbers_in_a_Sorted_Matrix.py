class Solution:
    @staticmethod
    def countNegatives(grid: list[list[int]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        i = 0  # rows
        j = cols - 1  # cols

        while 0 <= i < rows and 0 <= j < cols:
            if grid[i][j] < 0:
                count += rows - i
                j -= 1
            else:
                i += 1
        return count


def main():
    print(Solution.countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
    print(Solution.countNegatives([[3, 2], [1, 0]]))
    pass


if __name__ == '__main__':
    main()
