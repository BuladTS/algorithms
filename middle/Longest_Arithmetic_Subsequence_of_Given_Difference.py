class Solution:
    @staticmethod
    def longestSubsequence(arr: list[int], difference: int) -> int:
        dp = {}
        longest = 1
        for i in arr:
            prev = dp.get(i - difference, 0)
            dp[i] = prev + 1
            longest = max(longest, dp[i])
        return longest


def main():
    # print(Solution.longestSubsequence([1, 2, 3, 4], 1))
    # print(Solution.longestSubsequence([1, 3, 5, 7], 1))
    print(Solution.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))


if __name__ == "__main__":
    main()
