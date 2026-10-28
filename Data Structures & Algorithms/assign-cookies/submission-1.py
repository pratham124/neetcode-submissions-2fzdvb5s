class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        res = 0
        i = 0
        j = 0
        m = len(g)
        n = len(s)

        while i < m and j < n:
            if s[j] >= g[i]:
                res += 1
                i += 1
            j += 1


        return i