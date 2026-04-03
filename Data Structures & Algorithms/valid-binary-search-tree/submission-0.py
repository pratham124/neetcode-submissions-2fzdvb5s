# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res = []

        def dfs(n):
            nonlocal res
            if not n:
                return
            
            dfs(n.left)
            res.append(n.val)
            dfs(n.right)
        dfs(root)
        return res == sorted(set(res))