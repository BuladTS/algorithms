class Solution:
    @staticmethod
    def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        k = float('-inf')
        for start, end in intervals:
            if start >= k:
                k = end
            else:
                ans += 1
        return ans


def main():
    print(Solution.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
    print(Solution.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
    print(Solution.eraseOverlapIntervals([[1, 2], [2, 3]]))


if __name__ == "__main__":
    main()
