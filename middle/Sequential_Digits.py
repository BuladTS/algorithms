class Solution:
    @staticmethod
    def sequentialDigits(low: int, high: int) -> list[int]:
        res = []
        l = 0
        temp = low
        while temp:
            temp //= 10
            l += 1

        h = 0
        temp = high
        while temp:
            temp //= 10
            h += 1

        def gen(power):
            temp = 0
            temp_sup = 0
            j = 1
            for i in range(power, 0, -1):
                temp += j * 10 ** (i - 1)
                temp_sup += 1 * 10 ** (i - 1)
                j += 1
            return temp, temp_sup

        for i in range(l, h + 1):
            num, increment = gen(i)

            while num % 10 != 0:
                if low <= num <= high:
                    res.append(num)
                num += increment

        return res



def main():
    print(Solution.sequentialDigits(100, 300))
    print(Solution.sequentialDigits(1000, 13000))


if __name__ == '__main__':
    main()
