import collections


class Solution:
    @staticmethod
    def lengthOfLIS(nums: list[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
        # dp = collections.defaultdict(lambda x: [x, 1])
        # dp[nums[0]] = [nums[0], 1]
        # for i in range(1, len(nums)):
        #     for j in dp:
        #         if nums[i] > dp[j][0]:
        #             dp[j][1] += 1
        #     if nums[i] not in dp:
        #         dp[nums[i]] = [nums[i], 1]
        # return max(list(dp.values())[1])

        pass


def main():
    print(Solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print(Solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
    pass


if __name__ == "__main__":
    main()
