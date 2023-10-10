# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def deepestLeavesSum(root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return 0, 0

            res_left = dfs(node.left)
            res_right = dfs(node.right)
            if res_right == (0, 0) and res_left == (0, 0):
                return 1, node.val

            if res_right[0] == res_left[0]:
                return 1 + res_left[0], res_right[1] + res_left[1]
            elif res_left[0] > res_right[0]:
                return 1 + res_left[0], res_left[1]
            else:
                return 1 + res_right[0], res_right[1]

        return dfs(root)[1]


def main():
    print(Solution.deepestLeavesSum(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(7)), TreeNode(5)),
                                             TreeNode(3, None, TreeNode(6, None, TreeNode(8))))))



if __name__ == "__main__":
    main()
