# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> list[int]:
        self.res = []

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return

            self.res.append(node.val)
            dfs(node.right)
            dfs(node.left)

        dfs(root1)
        dfs(root2)
        self.res.sort()
        return self.res


def main():
    sol = Solution()
    print(sol.getAllElements(TreeNode(2, TreeNode(1), TreeNode(4)), TreeNode(1, TreeNode(0), TreeNode(3))))
    print(sol.getAllElements(TreeNode(1, None, TreeNode(8)), TreeNode(8, TreeNode(1))))


if __name__ == "__main__":
    main()

