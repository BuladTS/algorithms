import collections


class Solution:
    @staticmethod
    def evalRPN(tokens: list[str]) -> int:
        stack = collections.deque()
        operators = {'*', '/', '+', '-'}
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                first = stack.pop()
                second = stack.pop()
                if tokens[i] == '*':
                    stack.append(first * second)
                elif tokens[i] == '+':
                    stack.append(first + second)
                elif tokens[i] == '-':
                    stack.append(second - first)
                elif tokens[i] == '/':
                    stack.append(int(second / first))
        return stack.pop()


def main():
    # print(Solution.evalRPN(["2", "1", "+", "3", "*"]))
    # print(Solution.evalRPN(["4", "13", "5", "/", "+"]))
    print(Solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))


if __name__ == "__main__":
    main()
