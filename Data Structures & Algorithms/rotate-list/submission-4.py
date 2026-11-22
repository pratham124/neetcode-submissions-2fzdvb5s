# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        tail, n = head, 1
        while tail.next:
            n += 1
            tail = tail.next

        k = k % n

        if not k:
            return head
        
        cur = head
        for _ in range(n - k - 1):
            cur = cur.next
        
        newHead = cur.next
        tail.next = head
        cur.next = None
        return newHead



