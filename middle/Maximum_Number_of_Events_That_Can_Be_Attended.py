import heapq


class Solution:
    @staticmethod
    def maxEvents(events: list[list[int]]) -> int:
        events.sort(key=lambda x: (x[0], x[1]))
        last_day = 0
        for event in events:
            last_day = max(last_day, event[1])

        heap = []
        res = 0
        event_ind = 0

        n = len(events)
        for i in range(1, last_day + 1):

            while event_ind < n and events[event_ind][0] == i:
                heapq.heappush(heap, events[event_ind][1])
                event_ind += 1

            while heap and heap[0] < i:
                heapq.heappop(heap)

            if heap:
                res += 1
                heapq.heappop(heap)
        return res


def main():
    # print(Solution.maxEvents([[1, 2], [2, 3], [3, 4]]))
    print(Solution.maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]]))


if __name__ == '__main__':
    main()
