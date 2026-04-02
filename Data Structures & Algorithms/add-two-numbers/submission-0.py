# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        dummy = ListNode()
        dummyHead = dummy

        while l1 or l2 or remainder:
            total = remainder
            total += l1.val if l1 else 0
            total += l2.val if l2 else 0
            cur_val = total % 10
            remainder = total // 10
            dummy.next = ListNode(val=cur_val)
            dummy = dummy.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next