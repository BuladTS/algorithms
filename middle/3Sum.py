class Solution:
    @staticmethod
    def threeSum(nums: list[int]) -> list[list[int]]:

        res = set()
        seen = set()

        def two_sum(i):
            target = -nums[i]
            seen = set()

            for j in range(len(nums)):
                if i != j:
                    comp = target - nums[j]
                    if comp in seen:
                        res.add(tuple(sorted([nums[i], nums[j], comp])))
                    seen.add(nums[j])

        for i in range(len(nums)):
            if nums[i] not in seen:
                two_sum(i)
                seen.add(nums[i])
        return list(res)


if __name__ == '__main__':
    print(Solution.threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution.threeSum([0, 1, 1]))
    print(Solution.threeSum([0, 0, 0]))