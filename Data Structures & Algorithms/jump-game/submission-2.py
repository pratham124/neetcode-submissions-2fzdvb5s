class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        q = deque([0])


        target = len(nums) - 1
        visit = set()

        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur in visit:
                    continue
                visit.add(cur)
                if cur == target:
                    return True
                
                for j in range(1, nums[cur] + 1):
                    if (cur + j) in visit:
                        continue
                    q.append(cur + j)
        return False