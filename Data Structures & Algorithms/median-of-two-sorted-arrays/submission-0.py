class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        combined_arr = []

        first = 0
        second = 0
        n1 = len(nums1)
        n2 = len(nums2)

        while first < n1 and second < n2:
            if nums1[first] < nums2[second]:
                combined_arr.append(nums1[first])
                first += 1
            else:
                combined_arr.append(nums2[second])
                second += 1
        
        while first < n1:
            combined_arr.append(nums1[first])
            first += 1

        while second < n2:
            combined_arr.append(nums2[second])
            second += 1
        
        totalLen = len(combined_arr)
        if totalLen % 2 == 0:
            return (combined_arr[totalLen // 2 - 1] + combined_arr[totalLen // 2]) / 2.0
        else:
            return combined_arr[totalLen // 2]
            