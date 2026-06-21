class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ships = 1
            total = 0
            for w in weights:
                total += w
                if total > cap:
                    ships += 1
                    total = w
                    if ships > days:
                        return False
            
            return True



        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res