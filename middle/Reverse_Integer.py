class Solution:
    @staticmethod
    def reverse(x: int) -> int:

        if x > 0:
            is_postitive = True
        else:
            is_postitive = False
        result = 0
        zeros = True
        x = abs(x)
        while x >= 10:
            div = x % 10
            x = x // 10
            if div != 0 or not zeros:
                result = result * 10 + div
                zeros = False

        result = result * 10 + x
        if not is_postitive:
            result = - result
        if not (-2 ** 31 < result < 2 ** 31 - 1):
            return 0
        return result


if __name__ == "__main__":
    print(Solution.reverse(123))
    print(Solution.reverse(-123))
    print(Solution.reverse(120))
    print(Solution.reverse(10))
    print(Solution.reverse(90100))
    print(Solution.reverse(1534236469))

# [1, 2, 3, 7, 0, 0, 0]
# [2, 5, 6]

# [1, 2, 3, 0, 0, 0]
# [2, 5, 6]

