import collections


class Solution:
    @staticmethod
    def longestSemiRepetitiveSubstring(s: str) -> int:
        res = 0
        tab = [1]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                tab.append(1)
            else:
                tab[-1] = tab[-1] + 1
        for j in range(1, len(tab)):
            res = max(res, tab[j] + tab[j - 1])

        return max(res, tab[0])
        # dp = collections.defaultdict(lambda: -1)
        # i = 0
        # j = 0
        # back_num = ''
        # have_duplicate = False
        # max_length = float('-inf')
        # while j < len(s):
        #     if s[j] not in dp:
        #         dp[s[j]] = j
        #     else:
        #         back_num = s[j]
        #         if have_duplicate:
        #             i = dp[back_num]
        #             dp = collections.defaultdict(lambda: -1)
        #             if s[i] != s[j]:
        #                 have_duplicate = False
        #                 dp[s[j]] = i
        #             else:
        #                 dp[s[j]] = j
        #         else:
        #             have_duplicate = True
        #             dp[s[j]] = j
        #     max_length = max(max_length, j - i + 1)
        #     j += 1
        # return max_length


def main():
    print(Solution.longestSemiRepetitiveSubstring('52233'))
    print(Solution.longestSemiRepetitiveSubstring('5494'))
    print(Solution.longestSemiRepetitiveSubstring('1111111'))
    print(Solution.longestSemiRepetitiveSubstring('0010'))


if __name__ == "__main__":
    main()
