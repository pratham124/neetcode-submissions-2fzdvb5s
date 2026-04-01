class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_num = nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r-l) // 2
            min_num = min(min_num, nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1


        return min_num