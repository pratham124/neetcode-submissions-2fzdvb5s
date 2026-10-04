class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = set()
        
        def dfs(i, cur):
            nonlocal n, visited
            if len(cur) == n:
                res.append(cur.copy())
                return
            
            for j, nu in enumerate(nums):
                if j in visited:
                    continue
                visited.add(j)
                cur.append(nu)
                dfs(j, cur)
                visited.remove(j)
                cur.pop()

        dfs(0, [])
        return res