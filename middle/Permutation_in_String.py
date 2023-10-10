class Solution:
    @staticmethod
    def checkInclusion(s1: str, s2: str) -> bool:
        count_s1 = {}
        for i in s1:
            count_s1[i] = 1 + count_s1.get(i, 0)

        count = {}
        l = 0
        for r in range(len(s2)):
            if r - l + 1 > len(s1):
                count[s2[l]] -= 1
                l += 1
            count[s2[r]] = 1 + count.get(s2[r], 0)
            if s2[r] not in count_s1:
                count.pop(s2[r])
                l = r + 1
                count = {}
            if count == count_s1:
                return True

        return False


def main():
    print(Solution.checkInclusion('ab', 'eidboaoo'))
    print(Solution.checkInclusion('dtoj', 'zknhnruuqtjddnnqqeqkx'))


if __name__ == '__main__':
    main()

