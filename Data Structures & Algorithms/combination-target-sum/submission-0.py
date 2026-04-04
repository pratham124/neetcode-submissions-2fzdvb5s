class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(i, cur, cur_arr):
            nonlocal res
            if cur == target:
                res.append(cur_arr.copy())
                return
            if cur > target or i == n:
                return
            num = nums[i]
            cur_arr.append(num)
            dfs(i, cur + num, cur_arr)
            cur_arr.pop()
            dfs(i + 1, cur, cur_arr)
        dfs(0, 0, [])
        return res