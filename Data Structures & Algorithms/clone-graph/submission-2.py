"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        oldToNew = {}
        oldToNew[node] = Node(node.val)

        q = deque([node])

        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()
                for nei in cur_node.neighbors:
                    if nei not in oldToNew:
                        q.append(nei)
                        oldToNew[nei] = Node(nei.val)
                    oldToNew[cur_node].neighbors.append(oldToNew[nei])
        return oldToNew[node]



