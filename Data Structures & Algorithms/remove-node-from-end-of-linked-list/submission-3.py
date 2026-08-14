# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ahead = head
        dummy = ListNode(0, head)
        behind = dummy
        cur = head

        while n > 0:
            ahead = ahead.next
            n -= 1 

        while ahead:
            ahead = ahead.next
            behind = behind.next

        behind.next = behind.next.next
        return dummy.next


        