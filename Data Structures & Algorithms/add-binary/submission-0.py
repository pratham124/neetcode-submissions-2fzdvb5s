class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []

        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            cur_a = int(a[i]) if i >= 0 else 0
            cur_b = int(b[j]) if j >= 0 else 0
            total = cur_a + cur_b + carry
            res.append(total % 2)
            carry = total // 2

            i -= 1
            j -= 1
        res.reverse()
        return ''.join(map(str, res))