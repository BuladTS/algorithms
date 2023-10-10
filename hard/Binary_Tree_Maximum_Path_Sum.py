from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.answer = None

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = float('-inf')

        def helper(root_sup: Optional[TreeNode]) -> int:
            if root_sup is None:
                return 0

            left_max_sum = max(helper(root_sup.left), 0)
            right_max_sum = max(helper(root_sup.right), 0)
            self.answer = max(self.answer, left_max_sum + right_max_sum + root_sup.val)
            return max(left_max_sum, right_max_sum) + root_sup.val

        helper(root)
        return self.answer


def main():
    sol = Solution()
    print(sol.maxPathSum(TreeNode(1, TreeNode(2), TreeNode(3))))
    print(sol.maxPathSum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))


if __name__ == "__main__":
    main()
