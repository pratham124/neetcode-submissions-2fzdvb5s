class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                res = []
                while stack[-1] != "[":
                    res.append(stack.pop())
                stack.pop()
                res.reverse()
                multiple = ""
                while stack and stack[-1].isdigit():
                    multiple = stack.pop() + multiple
                multiple = int(multiple)
                stack.extend(res * multiple)
        return "".join(stack)


