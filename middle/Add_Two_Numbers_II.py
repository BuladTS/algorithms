# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []
        node = l1
        while node:
            s1.append(node.val)
            node = node.next

        node = l2
        while node:
            s2.append(node.val)
            node = node.next

        res = ListNode()
        plus_one = 0
        while s1 and s2:
            temp = s1.pop() + s2.pop()
            if plus_one:
                temp += 1
                plus_one = 0
            if temp >= 10:
                plus_one = 1
            res.val = temp % 10
            res = ListNode(0, res)

        while s1:
            temp = s1.pop()
            if plus_one:
                temp += 1
                plus_one = 0
            if temp >= 10:
                plus_one = 1
            res.val = temp % 10
            res = ListNode(0, res)

        while s2:
            temp = s2.pop()
            if plus_one:
                temp += 1
                plus_one = 0
            if temp >= 10:
                plus_one = 1
            res.val = temp % 10
            res = ListNode(0, res)
        if plus_one:
            res.val = 1
        return res.next if res.val == 0 else res


def main():
    l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    res = Solution.addTwoNumbers(l1, l2)
    while res:
        print(res.val, end=" ")
        res = res.next
    print("")
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(7, ListNode(6, ListNode(4)))
    res = Solution.addTwoNumbers(l1, l2)
    while res:
        print(res.val, end=" ")
        res = res.next

    print("")
    l1 = ListNode(0)
    l2 = ListNode(0)
    res = Solution.addTwoNumbers(l1, l2)
    while res:
        print(res.val, end=" ")
        res = res.next


if __name__ == "__main__":
    main()
