class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        seen = {}
        i = 0
        ans = 0
        for j in range(len(s)):
            if s[j] in seen:
                i = max(seen[s[j]] + 1, i)
            seen[s[j]] = j
            ans = max(ans, j - i + 1)
        return ans


if __name__ == "__main__":
    print(Solution.lengthOfLongestSubstring('abcabcbb'))
    print(Solution.lengthOfLongestSubstring('bbbbb'))
    print(Solution.lengthOfLongestSubstring('pwwkew'))

