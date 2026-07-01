# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        m = 0

        while curr:
            curr = curr.next
            m += 1

        if n == m:
            return head.next

        curr = head

        for _ in range(m - n - 1):
            curr = curr.next

        curr.next = curr.next.next

        return head