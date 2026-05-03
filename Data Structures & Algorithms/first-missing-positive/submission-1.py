class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            if 1 <= nums[i] <= n:
                correct_idx = nums[i] - 1
                if nums[correct_idx] != nums[i]:
                    nums[correct_idx], nums[i] = nums[i], nums[correct_idx]
                else:
                    i += 1
            else:
                i += 1

        for candidate in range(n):
            if nums[candidate] != candidate + 1:
                return candidate + 1
        return n + 1
