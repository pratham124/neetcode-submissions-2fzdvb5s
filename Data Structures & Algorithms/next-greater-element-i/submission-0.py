class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_element = {}

        stack = []

        for n in nums2:
            while stack and stack[-1] < n:
                greater_element[stack.pop()] = n
            stack.append(n)
        
        res = []
        for n in nums1:
            res.append(greater_element.get(n, -1))
        return res
