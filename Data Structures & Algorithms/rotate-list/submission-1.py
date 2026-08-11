# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        list_size = 0
        while cur:
            list_size += 1
            cur = cur.next
        k = k % list_size

        if not k:
            return head
        cur = head
        while k:
            prev = cur
            cur = cur.next
            k -= 1
        start = head
        prev = None
        while cur:
            prev = start
            cur = cur.next
            start = start.next
        prev.next = None

        second_prev = None
        new_head = start
        while start:
            second_prev = start
            start = start.next
        second_prev.next = head
        return new_head

        
        
    