class Solution:
    @staticmethod
    def maxProduct(nums: list[int]) -> int:
        res = float('-inf')
        cur_max, cur_min = 1, 1
        for x in nums:
            tmp = x * cur_max
            cur_max = max(x * cur_max, x * cur_min, x)
            cur_min = min(tmp, x * cur_min, x)
            res = max(res, cur_max)
            if x == 0:
                cur_max, cur_min = 1, 1
                continue

        return res


if __name__ == "__main__":
    # print(Solution.maxProduct([2, 3, -2, 4]))
    # print(Solution.maxProduct([-2, 0, -1]))
    print(Solution.maxProduct([-4, -3, -2]))
