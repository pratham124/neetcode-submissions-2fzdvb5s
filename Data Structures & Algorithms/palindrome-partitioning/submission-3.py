class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def dfs(i, cur):
            if i >= n:
                res.append(cur.copy())
                return
            
            for j in range(i, n):
                if not self.isPali(s, i, j):
                    continue
                cur.append(s[i:j + 1])
                dfs(j + 1, cur)
                cur.pop()
            
        dfs(0, [])
        return res

    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True