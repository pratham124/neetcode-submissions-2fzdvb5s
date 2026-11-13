class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + (customers[i - 1] == "N")

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + (customers[i] == 'Y')

        min_penalty = float('inf')
        res = 0

        for i in range(n + 1):
            penalty = prefix[i] + suffix[i]

            if penalty < min_penalty:
                min_penalty = penalty
                res = i

        return res