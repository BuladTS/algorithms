# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def same_tree(root1: Optional[TreeNode], root2: Optional[TreeNode]):
            if root1 is None and root2 is None:
                return True

            if root1 is None and root2 is not None:
                return False

            if root2 is None and root1 is not None:
                return False

            if root1.val != root2.val:
                return False

            return same_tree(root1.left, root2.left) and same_tree(root1.right, root2.right)

        return same_tree(p, q)


def main():
    print(Solution.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))))


if __name__ == '__main__':
    main()

