class Solution:
    @staticmethod
    def distributeCookies(cookies: list[int], k: int) -> int:
        min_unfairness = float("inf")
        dist = [0] * k

        def backtrack(i):
            nonlocal min_unfairness, dist
            if i == len(cookies):
                min_unfairness = min(min_unfairness, max(dist))
                return
            if min_unfairness <= max(dist):
                return

            for j in range(k):
                dist[j] += cookies[i]
                backtrack(i + 1)
                dist[j] -= cookies[i]

        backtrack(0)
        return min_unfairness


if __name__ == "__main__":
    print(Solution.distributeCookies([8, 15, 10, 20, 8], 2))
    print(Solution.distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3))
