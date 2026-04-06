class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]

        for i in range(len(strs[0]), -1, -1):
            prefix = strs[0][:i]
            valid = True
            for word in strs[1:]:
                if word[:i] != prefix:
                    valid = False
                    break
            if valid:
                return prefix
        return ""
        
       

