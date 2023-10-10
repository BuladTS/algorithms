import collections
import heapq


class Solution:
    @staticmethod
    def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        min_heap = [(0, k)]
        visit = set()
        t = 0
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(w1, t)
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(min_heap, (w1 + w2, n2))

        return t if len(visit) == n else -1


if __name__ == '__main__':
    print(Solution.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
