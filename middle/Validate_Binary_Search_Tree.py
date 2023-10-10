# Definition for a binary tree node.
from typing import Optional, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isValidBST(root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode], left: Union[int, float], right: Union[int, float]) -> bool:
            if node is None:
                return True

            if left < node.val < right:
                return dfs(node.left, left, min(right, node.val)) and \
                       dfs(node.right, max(left, node.val), right)
            else:
                return False

        return dfs(root, float('-inf'), float('inf'))


def main():
    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    print(Solution.isValidBST(tree))
    pass


if __name__ == '__main__':
    main()
