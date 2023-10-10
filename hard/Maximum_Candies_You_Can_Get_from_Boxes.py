class Solution:
    @staticmethod
    def maxCandies(status: list[int], candies: list[int], keys: list[list[int]],
                   containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        res = 0
        keys_have = set()
        visited = set()

        def helper(box):
            nonlocal res, keys_have, visited
            visited.add(box)
            res += candies[box]
            boxes = set(containedBoxes[box])
            for i in boxes:
                if status[i] == 1 or i in keys_have:
                    helper(i)

            for i in keys[box]:
                keys_have.add(i)

            for i in keys_have:
                if i not in visited and i in boxes:
                    helper(i)

        for initial in initialBoxes:
            helper(initial)

        return res


def main():
    # print(Solution.maxCandies(
    #     [1, 0, 1, 0],
    #     [7, 5, 4, 100],
    #     [[], [], [1], []],
    #     [[1, 2], [3], [], []],
    #     [0]
    # ))
    # print(Solution.maxCandies(
    #     [1, 0, 0, 0, 0, 0],
    #     [1, 1, 1, 1, 1, 1],
    #     [[1, 2, 3, 4, 5], [], [], [], [], []],
    #     [[1, 2, 3, 4, 5], [], [], [], [], []],
    #     [0]
    # ))
    print(Solution.maxCandies(
        [1, 1, 1],  # status
        [100, 1, 100],  # candies
        [[], [0, 2], []],  # keys
        [[], [], []],  # containedBoxes
        [1]  # initialBoxes
    ))


if __name__ == "__main__":
    main()
