class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r-l) // 2

            if nums[m] == target:
                return True

             # Right half is strictly sorted
            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

            # Left half is strictly sorted
            elif nums[m] > nums[r]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            # nums[m] == nums[r]: cannot determine the sorted half
            else:
                r -= 1

        return False