class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        dick = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dick:
                return [dick[diff], i]
            dick[n] = i