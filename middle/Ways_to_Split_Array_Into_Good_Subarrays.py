
# [1 0 0 0 0 1]
# [1] [0 0 0 0 1]
# [1 0] [0 0 0 1]
# [1 0 0] [0 0 1]
# [1 0 0 0] [0 1]
# [1 0 0 0 0] [1]

# [1 0 0 1]
# [1] [0 0 1]
# [1 0] [0 1]

# [0 1 1 0]

import bisect


class Solution:
    @staticmethod
    def numberOfGoodSubarraySplits(nums: list[int]) -> int:
        result = 1
        first_one_index = 0
        mod = int(1e9 + 7)
        while first_one_index < len(nums) and nums[first_one_index] != 1:
            first_one_index += 1

        if first_one_index == len(nums):
            return 0
        i = first_one_index + 1
        zeros = 1
        for i in range(i, len(nums)):
            if nums[i] == 1:
                result = (result * zeros) % mod
                zeros = 1
            else:
                zeros += 1
        return result


def main():
    # print(Solution.numberOfGoodSubarraySplits([0, 1, 0, 0, 1]))
    # print(Solution.numberOfGoodSubarraySplits([0, 1, 0, 0]))
    print(Solution.numberOfGoodSubarraySplits([0, 0, 0]))
    print(Solution.numberOfGoodSubarraySplits([0,1,1,1,0,0,1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,1,1,1,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,0,1,1,0]))


if __name__ == "__main__":
    main()
