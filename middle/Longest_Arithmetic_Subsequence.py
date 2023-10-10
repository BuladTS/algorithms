class Solution:
    @staticmethod
    def longestArithSeqLength(nums: list[int]) -> int:
        dp = [{} for _ in range(len(nums))]
        longest = 2
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                longest = max(longest, dp[i][diff])
        return longest


def main():
    print(Solution.longestArithSeqLength([3, 6, 9, 12]))
    print(Solution.longestArithSeqLength([9, 4, 7, 2, 10]))
    print(Solution.longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]))


if __name__ == '__main__':
    main()
