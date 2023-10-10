class Solution:
    @staticmethod
    def tallestBillboard(rods: list[int]) -> int:

        dp = {0: 0}

        for r in rods:
            new_dp = dp.copy()
            for diff, tallest in dp.items():
                shorter = tallest - diff

                new_dp[diff + r] = max(new_dp.get(diff + r, 0), tallest + r)

                new_diff = abs(shorter + r - tallest)
                new_tallest = max(shorter + r, tallest)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_tallest)

            dp = new_dp

        return dp.get(0, 0)


        # def dfs(index, sum1, sum2):
        #     if index == len(rods):
        #         return sum1 if sum1 == sum2 else 0
        #
        #     op1 = dfs(index + 1, sum1 + rods[index], sum2)
        #     op2 = dfs(index + 1, sum1, sum2 + rods[index])
        #     op3 = dfs(index + 1, sum1, sum2)
        #
        #     return max(op1, op2, op3)
        #
        # return dfs(0, 0, 0)


if __name__ == "__main__":
    print(Solution.tallestBillboard([1, 2, 3, 6]))
    print(Solution.tallestBillboard([1, 2, 3, 4, 5, 6]))
    print(Solution.tallestBillboard([1, 2]))
