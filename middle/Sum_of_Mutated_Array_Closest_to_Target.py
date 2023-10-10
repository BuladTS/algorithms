class Solution:
    @staticmethod
    def findBestValue(arr: list[int], target: int) -> int:
        arr.sort()
        n = len(arr)

        for i in range(len(arr)):
            sol = round(target / n)
            if arr[i] >= sol:
                return sol
            target -= arr[i]
            n -= 1
        return arr[-1]


def main():
    print(Solution.findBestValue([4, 9, 3], 10))
    print(Solution.findBestValue([2, 3, 5], 10))
    print(Solution.findBestValue([60864, 25176, 27249, 21296, 20204], 56803))


if __name__ == "__main__":
    main()
