# Definition for a binary tree node.
from tkinter.tix import Tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Integer:
    def __init__(self):
        self.i = 0

    def increment(self):
        self.i += 1


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def tree(root):
            if root is None:
                return 0, 0
            sum1, count1 = tree(root.left)
            sum2, count2 = tree(root.right)
            if root.val == (root.val + sum1 + sum2) // (count1 + count2 + 1):
                self.result += 1
            return root.val + sum1 + sum2, count1 + count2 + 1

        tree(root)
        return self.result
        # result = Integer()
        #
        # def count_sum(root):
        #     if root is None:
        #         return 0, 0
        #     left = count_sum(root.left)
        #     right = count_sum(root.right)
        #     return root.val + left[0] + right[0], 1 + left[1] + right[1]
        #
        # def count_average(root, res):
        #     if root is None:
        #         return res
        #     sum_root, roots = count_sum(root)
        #     print(sum_root)
        #     if (sum_root // roots) == root.val:
        #         res.increment()
        #     count_average(root.left, res)
        #     count_average(root.right, res)
        #
        # count_average(root, result)
        # return result.i


if __name__ == "__main__":
    sol = Solution()
    print(sol.averageOfSubtree(TreeNode(4, TreeNode(8, TreeNode(0), TreeNode(1)), TreeNode(5, None, TreeNode(6)))))
