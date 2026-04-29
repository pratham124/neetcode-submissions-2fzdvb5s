class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []

        l = 0
        r = len(nums) - 1

        while l <= r:
            left_num = nums[l] * nums[l]
            right_num = nums[r] * nums[r]

            if left_num > right_num:
                res.append(left_num)
                l += 1
            else:
                res.append(right_num)
                r -= 1
        return res[::-1]