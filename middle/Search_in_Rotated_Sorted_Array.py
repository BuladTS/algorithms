class Solution:
    @staticmethod
    def search(nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


def main():
    print(Solution.search([4, 5, 6, 7, 0, 1, 2], 0))
    print(Solution.search([4, 5, 6, 7, 0, 1, 2], 3))
    print(Solution.search([1], 0))


if __name__ == '__main__':
    main()
