class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(capacity):
            cur = 0
            d = 1
            for w in weights:
                if cur + w > capacity:
                    d += 1
                    cur = w
                    if d > days:
                        return False
                else:
                    cur += w
            return True

        while l <= r:
            m = l + (r - l ) // 2

            if canShip(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res