from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, temp = [], []

        def dfs(i):
            if i >= len(s):
                res.append(temp.copy())
                return
            for k in range(i, len(s)):
                if self.is_palindrome(s, i, k):
                    temp.append(s[i:k + 1])
                    dfs(k + 1)
                    temp.pop()
        dfs(0)
        return res

    def is_palindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


def main():
    sol = Solution()
    print(sol.partition("aab"))


if __name__ == '__main__':
    main()
