import collections

from numpy import zeros


def main():
    with open('input.txt', 'r') as file:
        len_line1 = int(file.readline())
        line1 = list(map(int, file.readline().split(' ')))  # 1 2 3
        len_line2 = int(file.readline())
        line2 = list(map(int, file.readline().split(' ')))  # 2 3 1
    dp = zeros((len_line1 + 1, len_line2 + 1), int)
    for i in range(1, len_line1 + 1):
        for j in range(1, len_line2 + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if line1[i - 1] == line2[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
    res = collections.deque()
    i = len_line1
    j = len_line2
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            res.appendleft(line1[i - 1])
            i -= 1
            j -= 1
    print(*res)


if __name__ == '__main__':
    main()



