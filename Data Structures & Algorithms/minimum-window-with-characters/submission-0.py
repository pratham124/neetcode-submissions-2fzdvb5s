class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        res = s + "t"

        t_count = defaultdict(int)
        for c in t:
            t_count[c] += 1
        s_count = defaultdict(int)
        matches = 0

        l = 0
        for r in range(len(s)):
            c = s[r]
            s_count[c] += 1

            if c in t_count and s_count[c] == t_count[c]:
                matches += 1
            print(s[l:r+1])
            print(matches)
            
            while matches == len(t_count):
                if (r - l + 1) < len(res):
                    res = s[l:r+1]
                s_count[s[l]] -= 1
                if s[l] in t_count and s_count[s[l]] < t_count[s[l]]:
                    matches -= 1
                l += 1

        if len(res) > len(s):
            return ""
        return res