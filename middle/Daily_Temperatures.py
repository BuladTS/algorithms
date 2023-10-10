class Solution:
    @staticmethod
    def dailyTemperatures(temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = (i - stackI)
            stack.append([t, i])

        return res


def main():
    print(Solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(Solution.dailyTemperatures([30, 40, 50, 60]))
    print(Solution.dailyTemperatures([30, 60, 90]))


if __name__ == "__main__":
    main()
