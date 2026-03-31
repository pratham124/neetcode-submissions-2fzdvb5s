class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        mp = {}
        l = 0
        r = 0

        while r < len(s):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        return res