import heapq


class Solution:
    @staticmethod
    def sortByBits(arr: list[int]) -> list[int]:

        def count_ones(n):
            count = 0
            while n:
                n = n & n - 1
                count += 1
            return count

        tmp = []
        for n in arr:
            ones = count_ones(n)
            tmp.append((ones, n))

        heapq.heapify(tmp)
        res = []
        while tmp:
            res.append(heapq.heappop(tmp)[1])
        return res


def main():
    print(Solution.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
    print(Solution.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))


if __name__ == '__main__':
    main()
