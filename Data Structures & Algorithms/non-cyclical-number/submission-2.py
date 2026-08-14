class Solution:
    def isHappy(self, n: int) -> bool:

        def square_sum(i):
            total = 0
            while i:
                digit = i % 10
                total += digit ** 2
                i = i // 10
            return total

        
        slow = n
        fast = square_sum(n)

        while True:
            if fast == 1:
                return True

            if slow == fast:
                return False


            slow = square_sum(slow)
            fast = square_sum(square_sum(fast))