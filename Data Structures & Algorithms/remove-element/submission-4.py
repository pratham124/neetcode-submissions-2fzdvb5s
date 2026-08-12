class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1 and val == nums[0]:
            return 0
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] != val:
                l += 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
        return l