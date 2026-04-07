class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {}

        for i, v in enumerate(nums):
            if v in num_dict and abs(num_dict[v] - i) <= k:
                return True
            num_dict[v] = i
        return False
        