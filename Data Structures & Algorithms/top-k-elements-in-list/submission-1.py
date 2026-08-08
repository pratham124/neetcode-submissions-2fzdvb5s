class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num in count.keys():
            buckets[count[num]].append(num)
        
        res = []
        for b in range(len(buckets) -1, -1, -1):
            for n in buckets[b]:
                res.append(n)
                k -= 1
                if not k:
                    return res
