class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def dfs(i, cur):
            nonlocal res
            if i == n:
                for p in cur:
                    if p != p[::-1]:
                        return
                res.append(cur.copy())
                return
            
            # concat the last element in array (check if palindrome)
            if cur:
                last_p = cur[-1]
                new_string = last_p + s[i]
                cur.pop()
                cur.append(new_string)
                dfs(i + 1, cur)
                cur.pop()
                cur.append(last_p)
            # append curr string in array
            cur.append(s[i])
            dfs(i +  1, cur)
            cur.pop()
        dfs(0, [])
        return res