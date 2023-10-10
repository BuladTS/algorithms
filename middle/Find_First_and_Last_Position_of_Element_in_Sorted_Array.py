class Solution:
    @staticmethod
    def searchRange(nums: list[int], target: int) -> list[int]:
        start, end = 0, len(nums)
        if end == 1 and target == nums[0]:
            return [0, 0]
        while True:
            mid = (start + end) // 2
            if start == mid and target != nums[mid]:
                return [-1, -1]
            if target == nums[mid]:
                break
            if target > nums[mid]:
                start = mid
            else:
                end = mid
        i, j = mid, mid
        while i - 1 >= 0 and nums[i - 1] == nums[mid]:
            i -= 1

        while j + 1 < len(nums) and nums[j + 1] == nums[mid]:
            j += 1
        return [i, j]


if __name__ == "__main__":
    # print(Solution.searchRange([5, 7, 7, 8, 8, 10], 8))
    # print(Solution.searchRange([5, 7, 7, 8, 8, 10], 6))
    print(Solution.searchRange([1, 3], 1))
