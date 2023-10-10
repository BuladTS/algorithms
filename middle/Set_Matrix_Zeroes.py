class Solution:
    @staticmethod
    def setZeroes(matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_0 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i == 0:
                        rows_0 = 0
                    else:
                        matrix[i][0] = 0

        def zeroes_col(col):
            for i in range(len(matrix)):
                matrix[i][col] = 0

        def zeroes_row(row):
            for j in range(len(matrix[0])):
                matrix[row][j] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                zeroes_row(i)
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                zeroes_col(i)
        if rows_0 == 0:
            zeroes_row(0)


def main():
    # matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    # Solution.setZeroes(matrix)
    # for i in matrix:
    #     print(i)

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution.setZeroes(matrix)
    for i in matrix:
        print(i)


if __name__ == "__main__":
    main()
