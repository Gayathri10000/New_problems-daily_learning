class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        
        for i in range(1,num+1):
            new_digit = sum(int(digit) for digit in str(i))
            # return new_digit
            if new_digit % 2 == 0:
                count+=1

        return count
