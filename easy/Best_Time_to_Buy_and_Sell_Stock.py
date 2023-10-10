class Solution:
    @staticmethod
    def maxProfit(prices: list[int]) -> int:
        max_profit = 0
        i = 0
        j = 0
        while j < len(prices):
            if prices[i] > prices[j]:
                i = j
            else:
                max_profit = max(max_profit, prices[i] - prices[j])
            j += 1
        return max_profit


if __name__ == '__main__':
    print(Solution.maxProfit([7, 1, 5, 3, 6, 4]))
