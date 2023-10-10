class Solution:
    @staticmethod
    def search(nums: list[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if mid == left:
                return -1
            if mid > target:
                right = mid
            else:
                left = mid


def main():
    # print(Solution.search([-1, 0, 3, 5, 9, 12], 9))
    # print(Solution.search([-1, 0, 3, 5, 9, 12], 2))
    print(Solution.search([2, 5], 2))


if __name__ == "__main__":
    main()
