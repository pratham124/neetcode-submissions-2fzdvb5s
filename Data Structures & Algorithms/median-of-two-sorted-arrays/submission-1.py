class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        sorted_arr = []

        n = len(nums1)
        m = len(nums2)
        cur1 = 0
        cur2 = 0

        while cur1 < n and cur2 < m:
            if nums1[cur1] < nums2[cur2]:
                sorted_arr.append(nums1[cur1])
                cur1 += 1
            else:
                sorted_arr.append(nums2[cur2])
                cur2 += 1
        
        if cur1 < n:
            sorted_arr.extend(nums1[cur1:])
        
        if cur2 < m:
            sorted_arr.extend(nums2[cur2:])
        
        m = len(sorted_arr) // 2
        if len(sorted_arr) % 2 == 1:
            return sorted_arr[m]
        else:
            return (sorted_arr[m] + sorted_arr[m-1]) / 2

        