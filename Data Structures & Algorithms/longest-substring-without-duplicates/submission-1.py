class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        count_dict = defaultdict(int)

        l = 0
        r = 0

        while r < len(s):
            count_dict[s[r]] += 1

            while count_dict[s[r]] > 1:
                count_dict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res