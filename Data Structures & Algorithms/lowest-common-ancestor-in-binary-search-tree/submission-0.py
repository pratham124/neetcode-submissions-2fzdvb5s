# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(n):
            if n.val == p.val or n.val == q.val:
                return n    
            if min(p.val, q.val) < n.val < max(p.val, q.val):
                return n
            
            if max(p.val, q.val) < n.val:
                return dfs(n.left)
            return dfs(n.right)
        return dfs(root)