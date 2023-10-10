def print_matrix(matrix):
    for i in matrix:
        print(i)


def main():
    with open("input.txt", "r") as file:
        rows, cols = map(int, file.readline().split(" "))
        matrix = [[] for _ in range(rows)]
        for i in range(rows):
            matrix[i] = list(map(int, file.readline().split(" ")))
    dp = [[(0, "") for _ in range(cols)] for _ in range(rows)]
    dp[0][0] = (matrix[0][0], '')
    for i in range(1, cols):
        dp[0][i] = (dp[0][i - 1][0] + matrix[0][i], dp[0][i - 1][1] + 'R')

    for i in range(1, rows):
        dp[i][0] = (dp[i - 1][0][0] + matrix[i][0], dp[i - 1][0][1] + 'D')

    for i in range(1, rows):
        for j in range(1, cols):
            if dp[i][j - 1][0] > dp[i - 1][j][0]:
                dp[i][j] = (dp[i][j - 1][0] + matrix[i][j], dp[i][j - 1][1] + 'R')
            else:
                dp[i][j] = (dp[i - 1][j][0] + matrix[i][j], dp[i - 1][j][1] + 'D')

    print(dp[-1][-1][0])
    print(' '.join(dp[-1][-1][1]))


if __name__ == "__main__":
    main()




