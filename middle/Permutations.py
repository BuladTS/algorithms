from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr: List, used: List):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    dfs(curr, used)
                    curr.pop()
                    used[i] = False
        dfs([], [False] * len(nums))
        return res

def main():
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.permute(nums))


if __name__ == '__main__':
    main()

