# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:  
        if not lists:
            return None
        while len(lists) > 1:
            list1 = lists.pop()
            list2 = lists.pop()
            dummyNode = ListNode(0)
            cur = dummyNode

            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                    cur = cur.next
                else:
                    cur.next = list2
                    list2 = list2.next
                    cur = cur.next
            
            if list1:
                cur.next = list1
            
            if list2:
                cur.next = list2

            lists.append(dummyNode.next)
        return lists[0]