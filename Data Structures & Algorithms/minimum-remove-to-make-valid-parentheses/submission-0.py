class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] not in ["(", ")"]:
                continue
            else:
                if s[i] == "(":
                    stack.append(i)
                elif stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        res = []
        
        for i in range(len(s) - 1, -1 , -1):
            if stack and i == stack[-1]:
                stack.pop()
            else:
                res.append(s[i])
        res.reverse()
        return "".join(res)