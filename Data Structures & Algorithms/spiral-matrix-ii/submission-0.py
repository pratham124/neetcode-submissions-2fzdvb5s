class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        l = 0 
        r = n - 1
        cur_val = 1
        while l <= r:
            top = l
            bottom = r
            for i in range(l, r + 1):
                mat[top][i] = cur_val
                cur_val += 1
            top += 1
            for i in range(top, bottom + 1):
                mat[i][r] = cur_val
                cur_val += 1
            r -= 1
            for i in range(r, l - 1, -1):
                mat[bottom][i] = cur_val
                cur_val += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                mat[i][l] = cur_val
                cur_val += 1
            l += 1

        return mat
