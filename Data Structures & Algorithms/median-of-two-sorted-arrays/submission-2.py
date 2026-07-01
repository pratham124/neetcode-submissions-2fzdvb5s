class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        smallArr = nums1 if len(nums1) < len(nums2) else nums2
        largeArr = nums1 if len(nums1) >= len(nums2) else nums2

        total = len(nums1) + len(nums2)
        half = total // 2

        l = 0
        r = len(smallArr) - 1

        while True:
            m = l + (r - l ) // 2
            other_m = half - m - 2

            smallLeft = smallArr[m] if m >= 0 else float("-infinity")
            smallRight = smallArr[m + 1] if m + 1 < len(smallArr) else float("infinity")
            largeLeft = largeArr[other_m] if other_m >= 0 else float("-infinity")
            largeRight = largeArr[other_m + 1] if other_m + 1 < len(largeArr) else float("infinity")

            if smallLeft <= largeRight and largeLeft <= smallRight:
                if total % 2:
                    return min(smallRight, largeRight)
                return (max(smallLeft, largeLeft) + min(smallRight, largeRight)) / 2
            elif smallLeft > largeRight:
                r = m - 1
            else:
                l = m + 1
