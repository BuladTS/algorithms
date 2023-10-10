class TrieNode:
    def __init__(self):
        self.children = {}
        self.isword = False

    def addWord(self, word: str):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isword = True



class Solution:
    @staticmethod
    def findWords(board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node: TrieNode, word):
            if (r < 0 or c < 0 or r == ROWS or c == COLS
                    or (r, c) in visited or board[r][c] not in node.children):
                return

            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isword:
                res.add(word)
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visited.remove((r, c))
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, '')

        return list(res)


def main():
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    print(Solution.findWords(board, words))


if __name__ == '__main__':
    main()
