class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i, v in enumerate(nums):
            if v != val:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        return k