# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_2_lists(list1: Optional[ListNode], list2: Optional[ListNode]):
    head = curr = ListNode()
    while list1 and list2:
        if list1.val > list2.val:
            curr.next = list2
            list2 = list2.next
        else:
            curr.next = list1
            list1 = list1.next
        curr = curr.next

    if list1:
        curr.next = list1
    if list2:
        curr.next = list2

    return head.next


class Solution:
    @staticmethod
    def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(merge_2_lists(l1, l2))
            lists = mergedLists

        return lists[0] if lists else []


def main():
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))

    res = Solution.mergeKLists([l1, l2, l3])
    while res:
        print(res.val, end=" ")
        res = res.next

    res = Solution.mergeKLists([None])


if __name__ == '__main__':
    main()

