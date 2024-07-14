class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        res = 0
        curr = 0
        n = len(customers)

        # Calculate the baseline satisfaction
        for index in range(n):
            if grumpy[index] == 0:
                res += customers[index]

        # Calculate initial extra satisfaction for the first window
        for index in range(minutes): 
            if grumpy[index] == 1:
                curr += customers[index]
        a = curr 

        # Slidjng window 
        for index in range(minutes,n):
            if grumpy[index] == 1:
                curr += customers[index]
            if grumpy[index-minutes] == 1:
                curr -= customers[index - minutes]
                
            a = max(curr,a)

        return a + res # output
