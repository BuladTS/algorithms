class Solution:
    @staticmethod
    def merge(intervals: list[list[int]]) -> list[list[int]]:
        result = []
        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0]
        for new_start, new_end in intervals:
            if end < new_start:
                result.append([start, end])
                start = new_start
                end = new_end
            elif end < new_end:
                end = new_end
        result.append([start, end])
        return result


def main():
    print(Solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(Solution.merge([[1, 4], [4, 5]]))


if __name__ == "__main__":
    main()
