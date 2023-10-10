# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    @staticmethod
    def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {None: None}

        cur = head
        while cur:
            seen[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            tmp = seen[cur]
            tmp.next = seen[cur.next]
            tmp.random = seen[cur.random]
            cur = cur.next
        return seen[head]


def main():
    pass


if __name__ == '__main__':
    main()
