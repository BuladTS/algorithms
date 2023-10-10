import bisect
import collections


class Solution:
    @staticmethod
    def makeArrayIncreasing(arr1: list[int], arr2: list[int]) -> int:
        dp = {-1: 0}
        arr2.sort()
        n = len(arr2)
        for i in range(len(arr1)):
            new_dp = collections.defaultdict(lambda: float('inf'))
            for prev in dp:
                if arr1[i] > prev:
                    new_dp[arr1[i]] = min(new_dp[arr1[i]], dp[prev])
                inx = bisect.bisect_right(arr2, prev)
                if inx < n:
                    new_dp[arr2[inx]] = min(new_dp[arr2[inx]], 1 + dp[prev])
            dp = new_dp
        return min(dp.values()) if dp else -1


def main():
    print(Solution.makeArrayIncreasing([1, 5, 3, 6, 7], [1, 3, 2, 4]))
    print(Solution.makeArrayIncreasing([1, 5, 3, 6, 7], [4, 3, 1]))
    print(Solution.makeArrayIncreasing([1, 5, 3, 6, 7], [1, 6, 3, 3]))


if __name__ == "__main__":
    main()
