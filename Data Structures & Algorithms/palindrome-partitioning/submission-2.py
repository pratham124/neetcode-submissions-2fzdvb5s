class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def dfs(i, cur):
            nonlocal res
            if i == n:
                res.append(cur.copy())
                return
            
            for j in range(i, n):
                if s[i:j+1] == s[i:j+1][::-1]:
                    cur.append(s[i:j+1])
                    dfs(j + 1, cur)
                    cur.pop()
            
            
        dfs(0, [])
        return res