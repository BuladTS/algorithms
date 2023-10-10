class Solution:
    @staticmethod
    def carFleet(target: int, position: list[int], speed: list[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort()

        stack = []
        for p, s in pair[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


def main():
    print(Solution.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print(Solution.carFleet(10, [3], [3]))
    print(Solution.carFleet(100, [0, 2, 4], [4, 2, 1]))


if __name__ == "__main__":
    main()
