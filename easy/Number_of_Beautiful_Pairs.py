class Solution:
    @staticmethod
    def countBeautifulPairs(nums: list[int]) -> int:
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if gcd(first_digit(nums[i]), nums[j] % 10) == 1:
                    count += 1
                    print(nums[i], nums[j])
        return count


def first_digit(num):
    while num > 10:
        num //= 10
    return num


def gcd(x, y):
    i = 2
    if x == y:
        return 2
    lim = round(x ** 0.5 if x < y else y ** 0.5) + 1
    while i <= lim:
        if x % i == 0 and y % i == 0:
            return 2
        i += 1
    return 1


if __name__ == "__main__":
    # print(Solution.countBeautifulPairs([2, 5, 1, 4]))
    # print(Solution.countBeautifulPairs([11, 21, 12]))
    # print(Solution.countBeautifulPairs(
    #     [756, 1324, 2419, 495, 106, 111, 1649, 1474, 2001, 1633, 273, 1804, 2102, 1782, 705, 1529, 1761, 1613, 111, 186,
    #      412]))
    print(Solution.countBeautifulPairs([756,1324,2419,495,106,111,1649,1474,2001,1633,273,1804,2102,1782,705,1529,1761,1613,111,186,412]))
