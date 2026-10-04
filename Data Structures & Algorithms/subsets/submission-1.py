class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)

        def dfs(i, cur):
            nonlocal res
            if i == n:
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
            dfs(i + 1, cur)

        dfs(0, [])
        return res