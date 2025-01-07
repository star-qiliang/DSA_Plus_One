
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stack = 0

        if digits[-1]+1<10:
            digits[-1]  = digits[-1] + 1
            return digits
        else: 
            digits[-1] = 0
            for j in range(len(digits)-2,-1,-1):
                if digits[j]+1>=10:
                    digits[j]=0
                else:
                    digits[j] = digits[j]+1
                    return digits

            digits = [1]+digits
            return digits


        