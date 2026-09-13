class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        n = len(nums)
        i = 0

        while i < n:
            if nums[i] == i + 1:
                i += 1
                continue
            else:
                cur_idx = nums[i] - 1
                if nums[i] == nums[cur_idx]:
                    i += 1
                else:
                    nums[i], nums[cur_idx] = nums[cur_idx], nums[i]
        
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res