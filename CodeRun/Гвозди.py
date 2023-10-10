import sys


def main():
    # n = int(input())
    # ls = list(map(int, input().split(' ')))
    n = 6
    ls = [3, 13, 12, 4, 14, 6]
    ls.sort()
    dp = [0 for _ in range(n)]
    if n == 2:
        res = abs(ls[0] - ls[1])
    else:
        dp[1] = ls[1] - ls[0]
        dp[2] = ls[2] - ls[0]
        for i in range(3, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + ls[i] - ls[i - 1]
        res = dp[-1]
    print(res)





if __name__ == '__main__':
    main()

