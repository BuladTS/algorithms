import collections


class Solution:
    @staticmethod
    def shortestPathAllKeys(grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        queue = collections.deque()

        # seen['key'] is only for BFS with key state equals 'keys'
        seen = collections.defaultdict(set)

        key_set, lock_set = set(), set()
        all_keys = 0
        start_r, start_c = -1, -1
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell in 'abcdef':
                    all_keys += (1 << (ord(cell) - ord('a')))
                    key_set.add(cell)
                if cell in 'ABCDEF':
                    lock_set.add(cell)
                if cell == "@":
                    start_r, start_c = i, j

        # [row, column, key_state, distance]
        queue.append((start_r, start_c, 0, 0))
        seen[0].add((start_r, start_c))

        while queue:
            cur_r, cur_c, keys, dist = queue.popleft()
            for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                new_r, new_c = cur_r + dr, cur_c + dc

                # If this cell (new_r, new_c) is reachable.
                if 0 <= new_r < m and 0 <= new_c < n and grid[new_r][new_c] != '#':
                    cell = grid[new_r][new_c]

                    # If it is a key we haven't picked up yet
                    if cell in key_set and not ((1 << (ord(cell) - ord('a'))) & keys):
                        new_keys = (keys | (1 << (ord(cell) - ord('a'))))

                        # If we collect all keys, return dist + 1.
                        # Otherwise, just add this state to seen and queue.
                        if new_keys == all_keys:
                            return dist + 1
                        seen[new_keys].add((new_r, new_c))
                        queue.append((new_r, new_c, new_keys, dist + 1))

                    # If it is a lock and we don't have its key, continue.
                    elif cell in lock_set and not (keys & (1 << (ord(cell) - ord('A')))):
                        continue

                    # We can walk to this cell if we haven't been here before with the same key state.
                    elif (new_r, new_c) not in seen[keys]:
                        seen[keys].add((new_r, new_c))
                        queue.append((new_r, new_c, keys, dist + 1))

        return -1
        # moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # m = len(grid)
        # n = len(grid[0])
        # q = collections.deque()
        # count = 0
        # for i in range(m):
        #     for j in range(n):
        #         char = grid[i][j]
        #         if char == '@':
        #             q.append((i, j, 0, 0))
        #         elif 'a' <= char <= 'f':
        #             count += 1
        #
        # keys = (1 << count) - 1
        # visited = set()
        # while q:
        #     x, y, steps, key = q.pop()
        #     if key == keys:
        #         return steps
        #     for m_x, m_y in moves:
        #         new_x = x + m_x
        #         new_y = y + m_y
        #         if 0 <= new_x <= m and 0 <= new_y <= m and grid[new_x][new_y] != '#':
        #             char = grid[new_x][new_y]
        #             if 'A' <= char <= 'F':
        #                 if (n >> (ord(char) - ord('A'))) & 1 == 1 and (new_x, new_y, key) not in visited:
        #                     visited.add((new_x, new_y, key))
        #                     q.append((new_x, new_y, steps + 1, key))
        #                 elif 'a' <= char <= 'f':
        #                     new_key = key | (1 << (ord(char) - ord('a')))
        #                     if (new_x, new_y, new_key) not in visited:
        #                         visited.add((new_x, new_y, new_key))
        #                         q.append((new_x, new_y, steps + 1, new_key))
        #                 else:
        #                     if (new_x, new_y, key) not in visited:
        #                         visited.add((new_x, new_y, key))
        #                         q.append((new_x, new_y, steps + 1, key))
        #
        # return -1


def main():
    print(Solution.shortestPathAllKeys(["@.a..", "###.#", "b.A.B"]))
    print(Solution.shortestPathAllKeys(["@..aA", "..B#.", "....b"]))
    print(Solution.shortestPathAllKeys(["@Aa"]))


if __name__ == "__main__":
    main()
