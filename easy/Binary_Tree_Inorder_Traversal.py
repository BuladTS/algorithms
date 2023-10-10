import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def inorderTraversal(root: Optional[TreeNode]) -> list[int]:
        res = []
        q_l = collections.deque()
        q_r = collections.deque()
        if root is None:
            return res
        q_l.append(root)
        while q_l:
            node = q_l.pop()
            res.append(node.val)
            if node.left:
                q_l.append(node.left)
            if node.right:
                q_r.append(node.right)
        while q_r:
            node = q_r.pop()
            res.append(node.val)

        return res


def main():
    print(Solution.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))


if __name__ == "__main__":
    main()