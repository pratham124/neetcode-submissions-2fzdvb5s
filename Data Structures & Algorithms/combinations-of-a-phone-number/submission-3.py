class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        n = len(digits)

        def dfs(i, cur):
            nonlocal res
            if i == n:
                res.append("".join(cur.copy()))
                return
            
            for c in digitToChar[digits[i]]:
                cur.append(c)
                dfs(i + 1, cur)
                cur.pop()

        dfs(0, [])

        return res