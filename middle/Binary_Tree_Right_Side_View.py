# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def rightSideView(root: Optional[TreeNode]) -> list[int]:
        res = []
        q = collections.deque()
        if root:
            q.append([root])

        while q:
            vals = collections.deque()
            level = q.pop()
            for i in range(len(level)):
                node = level[i]
                if node.left:
                    vals.append(node.left)
                if node.right:
                    vals.append(node.right)
            if vals:
                q.append(vals)
            res.append(level.pop().val)
        return res


def main():
    #    print(Solution.rightSideView(TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))))
    tree = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, TreeNode(6)))
    print(Solution.rightSideView(tree))


if __name__ == '__main__':
    main()
