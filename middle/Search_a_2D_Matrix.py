class Solution:
    @staticmethod
    def searchMatrix(matrix: list[list[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row * col - 1
        while left <= right:
            mid = (left + right) // 2
            num = matrix[mid // col][mid % col]
            if num == target:
                return True
            if num > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


def main():
    print(Solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(Solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))


if __name__ == "__main__":
    main()
