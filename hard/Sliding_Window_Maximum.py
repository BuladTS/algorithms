import collections


class Solution:
    @staticmethod
    def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
        res = []
        deque = collections.deque()
        l = r = 0
        while r < len(nums):
            while deque and nums[deque[-1]] < nums[r]:
                deque.pop()
            deque.append(r)

            if l > deque[0]:
                deque.popleft()

            if (r + 1) >= k:
                res.append(nums[deque[0]])
                l += 1
            r += 1

        return res


def main():
    print(Solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))


if __name__ == "__main__":
    main()
