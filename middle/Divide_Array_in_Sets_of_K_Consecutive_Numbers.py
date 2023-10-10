import collections


class Solution:
    @staticmethod
    def isPossibleDivide(nums: list[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        hash_map = collections.defaultdict(lambda: 0)
        max_nums = float('-inf')
        for i in nums:
            hash_map[i] += 1
            max_nums = max(max_nums, i)

        pointer = 1
        tracker = 0
        while pointer < max_nums + 1:
            if hash_map[pointer] == 0 and tracker == 0:
                pointer += 1
                continue
            if hash_map[pointer] == 0 and tracker != 0:
                return False
            hash_map[pointer] -= 1
            tracker += 1
            if tracker == k:
                tracker = 0
                pointer -= k

            pointer += 1
        return True if tracker == 0 else False


def main():
    # print(Solution.isPossibleDivide([1, 2, 3, 3, 4, 4, 5, 6], 4))
    # print(Solution.isPossibleDivide([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3))
    print(Solution.isPossibleDivide([1, 1, 2, 2, 3, 3], 2))


if __name__ == '__main__':
    main()
