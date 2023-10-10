def print_matrix(matrix):
    for i in matrix:
        print(i)


def main():
    with open('input.txt', 'r') as f:
        rows, cols = map(int, f.readline().split(' '))
        matrix = [0 for _ in range(rows)]
        for i in range(rows):
            matrix[i] = list(map(int, f.readline().split(' ')))

        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = matrix[0][0]
        for i in range(1, cols):
            dp[0][i] = dp[0][i - 1] + matrix[0][i]
        for j in range(1, rows):
            dp[j][0] = dp[j - 1][0] + matrix[j][0]

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
        print(dp[-1][-1])


if __name__ == '__main__':
    main()