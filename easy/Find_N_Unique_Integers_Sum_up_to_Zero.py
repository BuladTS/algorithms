class Solution:
    @staticmethod
    def sumZero(n: int) -> list[int]:
        arr = [0] * n
        half = n // 2
        i = 0
        for j in range(1, half + 1):
            arr[i] = -j
            arr[n - i - 1] = j
            i += 1
        if n % 2 == 1:
            arr[half] = 0
        return arr


def main():
    print(Solution.sumZero(5))
    print(Solution.sumZero(3))
    print(Solution.sumZero(1))
    print(Solution.sumZero(4))
    print(Solution.sumZero(6))


if __name__ == "__main__":
    main()
