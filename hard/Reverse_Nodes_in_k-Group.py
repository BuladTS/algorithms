# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[tuple[ListNode, ListNode]]:
    prev, curr = None, head
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev, head


class Solution:
    @staticmethod
    def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = slow = head
        prev_fast = None
        count = 1
        sup = head
        do = 0
        while fast:
            if count == k:
                tmp = fast.next
                fast.next = None
                fast = tmp
                prev, head_rev = reverse_list(slow)
                count = 1
                slow = fast
                head_rev.next = tmp

                if do == 0:
                    sup = prev
                    do += 1
                else:
                    prev_fast.next = prev

                prev_fast = head_rev
            else:
                count += 1
                fast = fast.next
        return sup


def main():
    ls = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = Solution.reverseKGroup(ls, 2)

    while res:
        print(res.val, end=" ")
        res = res.next


if __name__ == '__main__':
    main()

