def main():
    rows, cols = map(int, input().split(' '))
    dp = [[0 for i in range(cols)] for i in range(rows)]
    dp[0][0] = 1
    for i in range(rows):
        for j in range(cols):
            if 0 <= j - 1 < cols and 0 <= i - 2 < rows:
                dp[i][j] += dp[i - 2][j - 1]
            if 0 <= j - 2 < cols and 0 <= i - 1 < rows:
                dp[i][j] += dp[i - 1][j - 2]
    print(dp[-1][-1])


if __name__ == "__main__":
    main()
