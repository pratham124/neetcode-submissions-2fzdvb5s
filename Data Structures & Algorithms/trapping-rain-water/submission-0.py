class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        postfix = []

        tallest = 0
        for h in height:
            prefix.append(tallest)
            tallest = max(tallest, h)
        tallest = 0
        for i in range(len(height) -1, -1, -1):
            postfix.append(tallest)
            tallest = max(tallest, height[i])
        postfix.reverse()
        res = 0
        for i in range(len(height)):
            min_border = min(prefix[i], postfix[i])
            if min_border > height[i]:
                res += min_border - height[i]
        return res