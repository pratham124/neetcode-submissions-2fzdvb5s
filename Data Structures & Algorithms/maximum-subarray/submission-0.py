class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        prev = 0

        for n in nums:
            if prev < 0:
                prev = 0
            prev += n
            res = max(res, prev)
        return res