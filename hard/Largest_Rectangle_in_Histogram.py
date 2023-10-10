class Solution:
    @staticmethod
    def largestRectangleArea(heights: list[int]) -> int:
        stack = []  # (index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


def main():
    print(Solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(Solution.largestRectangleArea([2, 4]))


if __name__ == "__main__":
    main()
