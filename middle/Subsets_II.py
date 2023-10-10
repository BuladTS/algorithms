from typing import List


class Solution:
    @staticmethod
    def subsetsWithDup(nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(i: int, curr: List) -> None:
            if i == len(nums):
                res.append(curr.copy())
                return
            curr.append(nums[i])
            backtracking(i + 1, curr)
            curr.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtracking(i + 1, curr)

        backtracking(0, [])
        return res


def main():
    print(Solution.subsetsWithDup([1, 2, 2]))


if __name__ == "__main__":
    main()
