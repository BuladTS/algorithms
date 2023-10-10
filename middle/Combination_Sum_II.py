from typing import List


class Solution:
    @staticmethod
    def combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtracking(pos, curr: List, target):
            if target == 0:
                res.append(curr.copy())
            if target < 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if prev == candidates[i]:
                    continue
                curr.append(candidates[i])
                backtracking(i + 1, curr, target - candidates[i])
                curr.pop()
                prev = candidates[i]

        backtracking(0, [], target)
        return res


def main():
    print(Solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(Solution.combinationSum2([2, 5, 2, 1, 2], 5))


if __name__ == '__main__':
    main()
