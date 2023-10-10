class Solution:
    @staticmethod
    def productExceptSelf(nums: list[int]) -> list[int]:
        total = 1
        zeros = -1
        for i in range(len(nums)):
            if zeros == -1 and nums[i] == 0:
                zeros = i
            elif zeros != -1 and nums[i] == 0:
                return [0] * len(nums)
            else:
                total *= nums[i]
        res = []
        if zeros == -1:
            for i in nums:
                res.append(int(total / i))
            return res
        else:
            res = [0] * len(nums)
            res[zeros] = total
            return res


def main():
    print(Solution.productExceptSelf([1,2,3,4]))
    print(Solution.productExceptSelf([-1,1,0,-3,3]))


if __name__ == "__main__":
    main()
