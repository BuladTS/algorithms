import collections


def main():
    with open('input.txt', 'r') as file:
        tops, edges = map(int, file.readline().split())
        hash_map = collections.defaultdict(set)
        for _ in range(edges):
            frm, to = map(int, file.readline().split())
            hash_map[frm].add(to)
            hash_map[to].add(frm)
    visited = set()
    res = []

    def dfs(i, curr):
        if i in visited:
            return

        curr.append(i)
        visited.add(i)
        for j in hash_map[i]:
            dfs(j, curr)
        return curr

    for i in range(1, tops + 1):
        r = dfs(i, [])
        if r is not None:
            res.append(r)
    print(len(res))
    for i in res:
        print(len(i))
        print(' '.join(map(str, i)))



if __name__ == '__main__':
    main()
