import collections


class Solution:
    @staticmethod
    def longestConsecutive(nums: list[int]) -> int:
        seen = set(nums)
        res = 0
        for i in nums:
            if (i - 1) not in seen:
                l = 1
                while i + l in seen:
                    l += 1
                res = max(res, l)
        return res


def main():
    print(Solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(Solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))


if __name__ == "__main__":
    main()
