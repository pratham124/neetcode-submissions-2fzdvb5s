class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def dfs(cur, openN, closeN):
            if openN == closeN == n:
                res.append(cur)

            
            if closeN < openN:
                dfs(cur + ")", openN, closeN + 1)
            
            if openN < n:
                dfs(cur + "(", openN + 1, closeN)

        dfs("", 0, 0)
        return res