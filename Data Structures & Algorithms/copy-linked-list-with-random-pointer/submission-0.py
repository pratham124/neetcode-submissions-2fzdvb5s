"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        map_dict = {None: None}

        cur = head
        while cur:
            map_dict[cur] = Node(cur.val)
            cur = cur.next
        
        dummy = Node(0)
        dummyHead = dummy
        
        while head:
            newNode = map_dict[head]
            newNode.next = map_dict[head.next]
            newNode.random = map_dict[head.random]
            head = head.next
            dummyHead.next = newNode
            dummyHead = dummyHead.next

        return dummy.next