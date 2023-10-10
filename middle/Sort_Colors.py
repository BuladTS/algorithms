class Solution:
    @staticmethod
    def sortColors(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(nums, low, high):
            pivot = nums[(low + high) // 2]
            i = low - 1
            j = high + 1
            while True:
                i += 1
                while nums[i] < pivot:
                    i += 1

                j -= 1
                while nums[j] > pivot:
                    j -= 1

                if i >= j:
                    return j

                nums[i], nums[j] = nums[j], nums[i]

        def _quick_sort(items, low, high):
            if low < high:
                split_index = partition(items, low, high)
                _quick_sort(items, low, split_index)
                _quick_sort(items, split_index + 1, high)

        _quick_sort(nums, 0, len(nums) - 1)


def main():
    nums = [2, 0, 2, 1, 1, 0]
    Solution.sortColors(nums)
    print(nums)

    nums = [2, 0, 1]
    Solution.sortColors(nums)
    print(nums)


if __name__ == "__main__":
    main()
