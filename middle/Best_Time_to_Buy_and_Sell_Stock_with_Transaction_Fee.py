class Solution:
    @staticmethod
    def maxProfit(prices: list[int], fee: int) -> int:
        n = len(prices)
        hold, free = -prices[0], 0

        for i in range(1, n):
            tmp = hold
            hold = max(hold, free - prices[i])
            free = max(free, prices[i] + tmp - fee)

        return free


def main():
    print(Solution.maxProfit([1, 3, 2, 8, 4, 9], 2))
    print(Solution.maxProfit([1, 3, 7, 5, 10, 3], 3))


if __name__ == '__main__':
    main()
