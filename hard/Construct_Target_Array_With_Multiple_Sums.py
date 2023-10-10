class Solution:
    @staticmethod
    def isPossible(target: list[int]) -> bool:
        def helper(target):
            sum_array = 0
            max_value_index = 0

            for i in range(len(target)):
                sum_array += target[i]
                if target[max_value_index] < target[i]:
                    max_value_index = i
            diff = sum_array - target[max_value_index]
            if target[max_value_index] == 1 or diff == 1:
                return True

            if diff > target[max_value_index] or diff == 0 or target[max_value_index] % diff == 0:
                return False
            target[max_value_index] %= diff
            return helper(target)
        return helper(target)


def main():
    print(Solution.isPossible([9, 3, 5]))
    print(Solution.isPossible([1, 1, 1, 2]))
    print(Solution.isPossible([8, 5]))


if __name__ == '__main__':
    main()
