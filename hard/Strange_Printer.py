class Solution:
    @staticmethod
    def strangePrinter(s: str) -> int:
        if not s:
            return 0
        n = len(s)

        dp = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = dp[i + 1][j] + 1

                for k in range(i + 1, j + 1):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i][k - 1] + (dp[k + 1][j] if j > k else 0))

        return dp[0][n - 1]


def main():
    print(Solution.strangePrinter('aaabbb'))
    print(Solution.strangePrinter('aba'))


if __name__ == '__main__':
    main()

