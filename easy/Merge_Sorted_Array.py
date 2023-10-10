class Solution:
    @staticmethod
    def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0

        if n == 0:
            return

        while i < m:
            if nums1[i] > nums2[0]:
                temp = nums1[i]
                nums1[i] = nums2[0]
                nums2[0] = temp
                nums2.sort()
            i += 1
        while i < len(nums1):
            nums1[i] = nums2[j]
            j += 1
            i += 1


if __name__ == '__main__':
    arr = [1, 2, 3, 0, 0, 0]
    Solution.merge(arr, 3, [2, 5, 6], 3)
    print(arr)

    arr1 = [1]
    Solution.merge(arr1, 1, [], 0)
    print(arr1)
