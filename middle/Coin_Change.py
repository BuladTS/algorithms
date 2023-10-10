class Solution:
    @staticmethod
    def coinChange(coins: list[int], amount: int) -> int:

        memo = {}

        def helper(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')

            if amount in memo:
                return memo[amount]
            ret = float('inf')

            for c in coins:
                ret = min(ret, 1 + helper(amount - c))
            memo[amount] = ret
            return ret

        ans = helper(amount)
        return ans if ans != float('inf') else - 1


if __name__ == "__main__":
    print(Solution.coinChange([1, 2, 5], 11))
    print(Solution.coinChange([2], 3))