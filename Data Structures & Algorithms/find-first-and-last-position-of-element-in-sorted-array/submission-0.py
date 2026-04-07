class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                left_most = m
                right_most = m
                temp = m
                while m >= 0 and nums[m] == target:
                    left_most = m
                    m -= 1
                m = temp
                while m < n and nums[m] == target:
                    right_most = m
                    m += 1
                return [left_most, right_most]

            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return [-1, -1]