class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        remainder = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] = 0
                remainder += 1
            elif remainder:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    remainder = 0
            else:
                break
        
        if remainder:
            return [1] + digits
        return digits
