class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] <= 0 or nums[i] > n:
                i += 1
            else:
                correct_idx = nums[i] - 1
                if nums[i] == nums[correct_idx]:
                    i += 1
                else:
                    nums[correct_idx], nums[i] = nums[i], nums[correct_idx]
        
        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return n + 1