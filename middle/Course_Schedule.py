import collections


class Solution:
    @staticmethod
    def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
        hash_map = collections.defaultdict(list)
        for to, have_to in prerequisites:
            hash_map[to].append(have_to)

        visited = set()
        stack = set()

        def dfs(course):
            if course in stack:
                return True
            if course in visited:
                return False
            if course in hash_map:
                visited.add(course)
                stack.add(course)
                for i in hash_map[course]:
                    if dfs(i):
                        return True
                stack.remove(course)

            return False

        for i in range(numCourses):
            if dfs(i):
                return False
        return True


def main():
    # print(Solution.canFinish(2, [[1, 0]]))
    # print(Solution.canFinish(2, [[1, 0], [0, 1]]))
    print(Solution.canFinish(20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]))


if __name__ == "__main__":
    main()
