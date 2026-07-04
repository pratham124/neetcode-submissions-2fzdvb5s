# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:  
       
        minHeap = []
        heapq.heapify(minHeap)

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))

        dummy = ListNode(0)
        cur = dummy
        idx = len(lists)
        while minHeap:
            _, _, node = heapq.heappop(minHeap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, idx, node.next))
                idx += 1

        return dummy.next

