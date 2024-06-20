# Magnetic Force Between Two Balls

class Solution(object):
    def maxDistance(self, position, m):
        position.sort() #sorting the list
        n = len(position) #the length of the list

    
      '''as we take a list [1,2,4,5,6] 
         6 wille the (n-1) index and 1 be the first index the diff wille the max possibles
         and similary the min possibles '''
        maxi = position[n-1] - position[0]
        mini = position[1] - position[0]

        # the loop will start from the index two and  to the last val of the list
        for index in range(2,n):
            # find the minimum values
            mini = min(mini,position[index] - position[index-1])

        def ispossible(val):
            
            magneticballs = m-1 # decrementing the the giving m value as we palce the balls
            prev = 0 # intial pointer at 0 index
            
            for index in range(1,n): # loop start from the index 1 to n
                diff = position[index] - position[prev] 
                if diff >= val: #if the diff val is greater or equal then it is true
                    prev = index  
                    magneticballs -= 1 
                    if magneticballs == 0: # when the m value is equal to 0 then return true
                        return True

        res = -1 

        # the binary search  
        left,right = mini,maxi
        while left <= right:
            mid = (left+right) // 2 # mid value finding
            if ispossible(mid): # ispossible will be called and the mid value will be passed to the val parameter
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        return res # the final output
