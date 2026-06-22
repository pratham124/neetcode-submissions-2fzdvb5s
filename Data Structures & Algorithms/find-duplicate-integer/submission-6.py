class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for num in nums:
            cur = abs(num)
            if nums[cur - 1] < 0:
                return cur
            nums[cur - 1] *= -1
        
            