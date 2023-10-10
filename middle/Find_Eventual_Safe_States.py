class Solution:
    def __init__(self):
        self.visited = None
        self.inStack = None
        self.graph = None

    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        length = len(graph)
        self.graph = graph
        self.inStack = [False] * length
        self.visited = [False] * length
        for i in range(length):
            self.dfs(i)

        res = []
        for i in range(length):
            if not self.inStack[i]:
                res.append(i)
        return res

    def dfs(self, index: int):
        if self.inStack[index]:
            return True
        if self.visited[index]:
            return False
        self.inStack[index] = True
        self.visited[index] = True
        for neighbor in self.graph[index]:
            if self.dfs(neighbor):
                return True

        self.inStack[index] = False
        return False


def main():
    sol = Solution()
    print(sol.eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
    print(sol.eventualSafeNodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))


if __name__ == "__main__":
    main()
