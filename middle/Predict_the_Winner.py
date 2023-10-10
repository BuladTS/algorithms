class Solution:
    @staticmethod
    def PredictTheWinner(nums: list[int]) -> bool:
        n = len(nums)
        dp = [[0] * (len(nums)) for _ in range(len(nums))]
        for i in range(n):
            dp[i][i] = nums[i]

        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left][right] = max(nums[left] - dp[left + 1][right], nums[right] - dp[left][right - 1])

        return dp[0][n - 1] >= 0


def main():
    print(Solution.PredictTheWinner([1, 5, 2]))
    print(Solution.PredictTheWinner([1, 5, 233, 7]))

# [1, 2, 3, 5]


if __name__ == '__main__':
    main()
