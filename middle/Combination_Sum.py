import copy


class Solution:
    @staticmethod
    def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
        res = []
        if len(candidates) == 0:
            return res
        candidates.sort()
        combination = []
        dfs(res, combination, candidates, target, 0)
        return res


def dfs(results, combination, candidates, target, start_index):
    if target == 0:
        results.append(copy.deepcopy(combination))
        return

    for i in range(start_index, len(candidates)):
        if candidates[i] > target:
            break

        combination.append(candidates[i])
        dfs(results, combination, candidates, target - candidates[i], i)
        combination.pop()


def main():
    print(Solution.combinationSum([2, 3, 6, 7], 7))
    print(Solution.combinationSum([2, 3, 5], 8))
    print(Solution.combinationSum([2], 1))


if __name__ == "__main__":
    main()
