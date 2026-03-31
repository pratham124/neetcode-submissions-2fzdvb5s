class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        freq_dict = defaultdict(int)
        res = 0
        for r in range(len(s)):
            freq_dict[s[r]] += 1
            while (r - l + 1 - max(freq_dict.values())) > k:
                freq_dict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res