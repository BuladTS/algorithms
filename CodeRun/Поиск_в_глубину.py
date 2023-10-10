def main():
    with open('input.txt', 'r') as file:
        nodes, edges = map(int, file.readline().split())
        ways = [[False for _ in range(nodes + 1)] for _ in range(nodes + 1)]
        for _ in range(edges):
            node_1, node_2 = map(int, file.readline().split())
            ways[node_1][node_2] = True
            ways[node_2][node_1] = True
    res = []
    visited = set()

    def dfs(node):
        nonlocal res, visited
        if node in visited:
            return
        visited.add(node)
        res.append(node)
        for i in range(1, nodes + 1):
            if ways[i][node]:
                dfs(i)
    dfs(1)
    print(len(res))
    print(*sorted(res))


if __name__ == '__main__':
    main()
