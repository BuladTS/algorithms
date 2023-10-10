from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        def func(p: Optional[ListNode], c: Optional[ListNode]):
            tmp = c.next
            c.next = p
            pr = c
            if not tmp:
                return c
            cr = tmp
            return func(pr, cr)

        return func(prev, curr)


def main():
    res = Solution.reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    while res:
        print(res.val, end=' ')
        res = res.next


if __name__ == "__main__":
    main()

