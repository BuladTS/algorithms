class Solution:
    @staticmethod
    def numberOfSubstrings(s: str) -> int:
        a = b = c = 0
        ans, i, n = 0, 0, len(s)

        for j in range(n):
            if s[j] == 'a':
                a += 1
            elif s[j] == 'b':
                b += 1
            else:
                c += 1

            while a > 0 and b > 0 and c > 0:
                ans += n - j
                if s[i] == 'a':
                    a -= 1
                elif s[i] == 'b':
                    b -= 1
                else:
                    c -= 1
                i += 1
        return ans


def main():
    print(Solution.numberOfSubstrings('abcabc'))
    print(Solution.numberOfSubstrings('aaacb'))
    print(Solution.numberOfSubstrings('abc'))


if __name__ == '__main__':
    main()
