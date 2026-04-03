# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True
        if not root:
            return is_balanced
        

        def dfs(n):
            nonlocal is_balanced

            if not n:
                return 0

            l = dfs(n.left)
            r = dfs(n.right)

            if abs(l - r) > 1:
                is_balanced = False
            return 1 + max(l, r)

        dfs(root)
        return is_balanced