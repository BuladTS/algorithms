class Solution:
    @staticmethod
    def fourSum(nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res, quad = [], []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return

            l, r = start, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        kSum(4, 0, target)
        return res


def main():
    print(Solution.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(Solution.fourSum([2, 2, 2, 2, 2], 8))


if __name__ == "__main__":
    main()
