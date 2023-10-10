import math


class Solution:
    @staticmethod
    def minEatingSpeed(piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res


def main():
    print(Solution.minEatingSpeed([3, 6, 7, 11], 8))
    print(Solution.minEatingSpeed([30, 11, 23, 4, 20], 5))


if __name__ == '__main__':
    main()
