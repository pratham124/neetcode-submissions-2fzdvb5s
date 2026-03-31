class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        if len(prices) == 1:
            return 0
        
        l = 0
        r = 1

        while r < len(prices):
            cur_price = prices[r] - prices[l]
            if cur_price > 0:
                res = max(cur_price, res)
            else:
                l = r
            r += 1
        return res
