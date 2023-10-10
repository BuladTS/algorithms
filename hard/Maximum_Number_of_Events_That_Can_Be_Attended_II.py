import collections


class Solution:
    @staticmethod
    def maxValue(events: list[list[int]], k: int) -> int:
        n = len(events)
        events.sort()

        def dfs(i, prev_end, count):
            if i == n or count == k:
                return 0

            best = dfs(i + 1, prev_end, count)

            if events[i][0] > prev_end:
                best = max(best, events[i][2] + dfs(i + 1, events[i][1], count + 1))
            return best

        return dfs(0, 0, 0)


def main():
    print(Solution.maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2))
    print(Solution.maxValue([[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2))
    print(Solution.maxValue([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 3))
    q = collections.deque


if __name__ == "__main__":
    main()
