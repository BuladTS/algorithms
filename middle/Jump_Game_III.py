import collections


class Solution:
    @staticmethod
    def canReach(arr: list[int], start: int) -> bool:
        memo = collections.defaultdict(bool)

        def dfs(index: int):
            if index in memo:
                return memo[index]
            if arr[index] == 0:
                memo[index] = True
            else:
                memo[index] = False
            if index + arr[index] < len(arr) and index + arr[index] not in memo:
                dfs(index + arr[index])
            if index - arr[index] >= 0 and index - arr[index] not in memo:
                dfs(index - arr[index])
            return False
        dfs(start)
        return True in memo.values()


def main():
    print(Solution.canReach([4, 2, 3, 0, 3, 1, 2], 5))
    print(Solution.canReach([4, 2, 3, 0, 3, 1, 2], 0))
    print(Solution.canReach([3, 0, 2, 1, 2], 2))


if __name__ == "__main__":
    main()
