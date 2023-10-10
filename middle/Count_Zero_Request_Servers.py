class Solution:
    @staticmethod
    def countServers(n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda element: element[1])
        result = []
        # print(logs)
        # print(find_first_index(logs, 6))
        for q in queries:
            servers = set()
            first_index = find_first_index(logs, q - x)
            last_index = find_last_index(logs, q)
            for i in range(first_index, last_index + 1):
                servers.add(logs[i][0])
            result.append(n - len(servers))
        return result


def find_last_index(logs: list[list[int]], value):
    if logs[0][1] > value:
        return -1
    if logs[-1][1] < value:
        return len(logs) - 1
    low = 0
    high = len(logs)
    mid = (low + high) // 2
    while True:
        if value == logs[mid][1]:
            break
        if low == mid:
            break
        if value > logs[mid][1]:
            low = mid
            mid = (low + high) // 2
        else:
            high = mid
            mid = (low + high) // 2
    while logs[mid][1] > value:
        mid -= 1
    return mid


def find_first_index(logs: list[list[int]], value):
    if logs[-1][1] < value:
        return -1
    low = 0
    high = len(logs)
    mid = (low + high) // 2
    while True:
        if value == logs[mid][1]:
            break
        if low == mid:
            break
        if value > logs[mid][1]:
            low = mid
            mid = (low + high) // 2
        else:
            high = mid
            mid = (low + high) // 2

    while logs[mid][1] < value:
        mid += 1

    while logs[mid][1] > value and mid != 0:
        mid -= 1

    while logs[mid][1] == logs[mid - 1][1]:
        mid -= 1
    return mid


if __name__ == "__main__":
    # print(Solution.countServers(3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11]))
    # print(Solution.countServers(3, [[2, 4], [2, 1], [1, 2], [1, 2], [3, 1], [1, 2]], 2, [3, 4]))
    print(Solution.countServers(4, [[2, 30], [2, 5], [3, 9], [4, 21]], 9, [11, 28, 16, 18]))
