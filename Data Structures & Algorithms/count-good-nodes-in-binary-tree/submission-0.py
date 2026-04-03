# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0

        def dfs(n, maxVal):
            nonlocal res
    
            if not n:
                return
            
            if n.val >= maxVal:
                maxVal = n.val
                res += 1
            dfs(n.left, maxVal)
            dfs(n.right, maxVal)


        dfs(root, -101)
        return res