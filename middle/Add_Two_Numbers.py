# [9, 9, 9, 9, 9, 9, 9]
# [9, 9, 9, 9]
# [8, 9, 9, 9, 0, 0, 0, 1]


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res

        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            add = l1_val + l2_val + carry

            carry = add // 10
            mod = add % 10

            cur.next = ListNode(mod)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res.next


def main():
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))

    res = Solution.addTwoNumbers(l1, l2)
    while res is not None:
        print(f'{res.val} ', end="")
        res = res.next
    print("")

    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

    res = Solution.addTwoNumbers(l1, l2)
    while res is not None:
        print(f'{res.val} ', end="")
        res = res.next


if __name__ == "__main__":
    main()




