class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)

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
        
        while stack:
            s[stack.pop()] = ''
        return "".join(s)