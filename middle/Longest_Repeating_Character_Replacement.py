class Solution:
    @staticmethod
    def characterReplacement(s: str, k: int) -> int:
        count = {}

        l = 0
        max_sign = 0

        res = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_sign = max(max_sign, count[s[r]])

            if (r - l + 1) - max_sign > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


def main():
    print(Solution.characterReplacement("AABABBA", 1))


if __name__ == '__main__':
    main()
