from collections import deque


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        parentheses = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        q = deque()
        ans = False
        for i in s:
            if i in parentheses:
                q.append(parentheses[i])
            elif len(q) > 0:
                if q.pop() != i:
                    return False
                else:
                    ans = True
            else:
                return False
        if len(q) != 0:
            return False
        return ans


if __name__ == '__main__':
    # print(Solution.isValid("()"))
    # print(Solution.isValid("()[]{}"))
    # print(Solution.isValid("(]"))
    # print(Solution.isValid("([)]"))
    print(Solution.isValid("([]){"))
