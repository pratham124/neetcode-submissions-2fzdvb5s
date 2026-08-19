# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        groups = 0
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
        groups = cnt // k

        if not groups or k == 1:
            return head

        prev = None
        cnt = 0
        curHead = None
        dummyNode = ListNode()
        prevHead = dummyNode
        curHead = None
        cur = head
        while groups:
            cnt += 1
            if cnt == 1:
                curHead = cur
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            if cnt == k:
                cnt = 0
                groups -= 1
                prevHead.next = prev
                prev = None
                prevHead = curHead
        
        if cur:
            prevHead.next = cur

        return dummyNode.next
