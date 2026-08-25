class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        mp = {}
        for r in range(len(nums)):
            cur_num = nums[r]
            if cur_num in mp and mp[cur_num] >= l:
                return True
            mp[cur_num] = r

            if r - l + 1 == k + 1:
                l += 1
        return False
