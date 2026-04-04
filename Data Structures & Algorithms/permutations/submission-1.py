class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visit = set()

        def dfs(i, cur):
            nonlocal visit
            if len(cur) == n:
                res.append(cur.copy())
                return
            for i in range(n):
                if i in visit:
                    continue
                visit.add(i)
                cur.append(nums[i])
                dfs(i, cur)
                visit.remove(i)
                cur.pop()


        dfs(0, [])
        return res