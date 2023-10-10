import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:


    @staticmethod
    def serialize(root: TreeNode) -> str:
        res = []

        def dfs(node: Optional[TreeNode]):
            if node is None:
                res.append(str(node))
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ','.join(res)

    @staticmethod
    def deserialize(data: str) -> Optional[TreeNode]:
        q = collections.deque(data.split(','))
        root_val = q.popleft()
        if root_val == 'None':
            return None
        root = TreeNode(int(root_val))

        def dfs(node: TreeNode):
            val = q.popleft()
            if val == 'None':
                node.left = None
                val = q.popleft()
                if val == 'None':
                    node.right = None
                    return
                else:
                    node.right = TreeNode(int(val))
                    dfs(node.right)
                return
            else:
                node.left = TreeNode(int(val))
                dfs(node.left)
            val = q.popleft()
            if val == 'None':
                node.right = None
            else:
                node.right = TreeNode(int(val))
                dfs(node.right)

        dfs(root)
        return root


def main():
    tree = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(9, None, TreeNode(7)))), TreeNode(3))
    serialized = Codec.serialize(tree)
    print(Codec.serialize(tree))
    print(Codec.serialize(Codec.deserialize(serialized)))


if __name__ == "__main__":
    main()
