class Solution:
    @staticmethod
    def uniquePaths(m: int, n: int) -> int:
        old_row = [1] * n
        for row in range(1, m):
            new_row = [1] * n
            for col in range(1, n):
                new_row[col] = new_row[col - 1] + old_row[col]
            old_row = new_row
        return old_row[-1]


def main():
    print(Solution.uniquePaths(3, 7))
    print(Solution.uniquePaths(3, 2))


if __name__ == "__main__":
    main()
