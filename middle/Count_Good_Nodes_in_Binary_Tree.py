# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def goodNodes(root: TreeNode) -> int:
        res = 1

        def dfs(node: Optional[TreeNode], max_val: int):
            nonlocal res
            if node is None:
                return
            if node.val >= max_val:
                res += 1
            dfs(node.right, max(node.val, max_val))
            dfs(node.left, max(node.val, max_val))

        dfs(root.left, root.val)
        dfs(root.right, root.val)

        return res


def main():
    tree = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    print(Solution.goodNodes(tree))


if __name__ == '__main__':
    main()
