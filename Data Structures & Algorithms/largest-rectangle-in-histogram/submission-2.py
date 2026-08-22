class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            cur_idx = i
            while stack and stack[-1][1] > h:
                idx, hei = stack.pop()
                cur_idx = idx
                width = i - idx
                maxArea = max(maxArea, width * hei)
            maxArea = max(maxArea, h)
            stack.append((cur_idx, h))
        
        for i, h in stack:
            width = len(heights) - i
            maxArea = max(maxArea, width * h)
        return maxArea