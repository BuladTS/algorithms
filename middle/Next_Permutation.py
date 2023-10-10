class Solution:
    @staticmethod
    def nextPermutation(nums: list[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(start):
            end = len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        i = len(nums) - 2
        while i != -1 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            reverse(i + 1)
            return nums

        j = i
        while j + 1 != len(nums) and nums[j + 1] > nums[i]:
            j += 1

        nums[i], nums[j] = nums[j], nums[i]

        reverse(i + 1)
        return nums


def main():
    print(Solution.nextPermutation([1, 2, 3]))
    print(Solution.nextPermutation([3, 2, 1]))
    print(Solution.nextPermutation([1, 1, 5]))


if __name__ == "__main__":
    main()
