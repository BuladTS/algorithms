class Solution:
    @staticmethod
    def xorQueries(arr: list[int], queries: list[list[int]]) -> list[int]:
        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        ans = []
        for start, end in queries:
            if start == 0:
                ans.append(arr[end])
            else:
                ans.append(arr[end] ^ arr[start - 1])
        return ans


def main():
    print(Solution.xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]))
    print(Solution.xorQueries([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]))


if __name__ == "__main__":
    main()
