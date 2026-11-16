class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        res = []

        q = deque()
        for r, n in enumerate(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            while (r - q[0] + 1) > k:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
            
        return res
