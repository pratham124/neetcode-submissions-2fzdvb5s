class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        char_arr = [0] * 26
        for c in s1:
            idx = ord(c) - ord('a')
            char_arr[idx] += 1
        
        for i in range(len(s1)):
            idx = ord(s2[i]) - ord('a')
            char_arr[idx] -= 1



        l = 0
        for r in range(len(s1), len(s2)): 
            if min(char_arr) == 0 and max(char_arr) == 0:
                return True
            
            l_idx = ord(s2[l]) - ord('a')
            r_idx = ord(s2[r]) - ord('a')
            char_arr[l_idx] += 1
            char_arr[r_idx] -= 1
            l += 1
        if min(char_arr) == 0 and max(char_arr) == 0:
            return True
        return False

            
