class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)    
        res = 0
        for n in num_set:
            if n - 1 not in num_set:
                l = n
                r = n
                while r in num_set:
                    r += 1
                res = max(res, r - l)
        return res