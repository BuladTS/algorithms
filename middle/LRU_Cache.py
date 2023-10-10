class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right

        prev.next = node
        node.prev = prev

        nxt.prev = node
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.data:
            self.remove(self.data[key])
            self.insert(self.data[key])
            return self.data[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.remove(self.data[key])
        self.data[key] = Node(key, value)
        self.insert(self.data[key])

        if self.capacity < len(self.data):
            del self.data[self.left.next.key]
            self.remove(self.left.next)

