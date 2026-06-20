class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr1, arr2):
            res = []
            n = len(arr1)
            m = len(arr2)
            l = r = 0
            while l < n and r < m:
                if arr1[l] < arr2[r]:
                    res.append(arr1[l])
                    l += 1
                else:
                    res.append(arr2[r])
                    r += 1
            
            if l < n:
                res.extend(arr1[l:])
            
            if r < m:
                res.extend(arr2[r:])
            return res

        def mergeSort(arr):
            if len(arr) <= 1:
                return arr
            
            m = len(arr) // 2
            l = mergeSort(arr[:m])
            r = mergeSort(arr[m:])
            return merge(l, r)

        
        return mergeSort(nums)
            
