class Solution:
    @staticmethod
    def minimizeConcatenatedLength(words: list[str]) -> int:
        memo = {}
        answer = dfs(words, 1, words[0][0], words[0][-1], memo)
        return answer + len(words[0])


def dfs(words, idx, left, right, memo):
    if idx == len(words):
        return 0
    if (idx, left, right) in memo:
        return memo[(idx, left, right)]

    length = float("inf")
    if words[idx][-1] == left:
        length = min(length, dfs(words, idx + 1, words[idx][0], right, memo) + (len(words[idx]) - 1))
    else:
        length = min(length, dfs(words, idx + 1, words[idx][0], right, memo) + len(words[idx]))
    if words[idx][0] == right:
        length = min(length, dfs(words, idx + 1, left, words[idx][-1], memo) + (len(words[idx]) - 1))
    else:
        length = min(length, dfs(words, idx + 1, left, words[idx][-1], memo) + len(words[idx]))
    memo[(idx, left, right)] = length
    return length


if __name__ == "__main__":
    print(Solution.minimizeConcatenatedLength(["aa","bc","bb"]))
