''' 
    INPUT : height = [1,8,6,2,5,4,8,3,7]
    OUTPUT : 49

As 
the area of rectangle is height * width but the input as height but width, simple the diff between the two heights
we take the left(i) and right(j) the two-pointers pointing to  first and last index in the given list respectively.

 0 1 2 3 4 5 6 7 8 = (INDEX)
 1 8 6 2 5 4 8 3 7                         WIDTH = j-i = 8-0 = 8 , HEIGHT = min(height(i),height(j)) = min(1,7) = 1
 i               j                         AREA = WIDTH * HEIGHT = 8*1 = 8

 1 8 6 2 5 4 8 3 7                         WIDTH = j-i = 8-1 = 7 , HEIGHT = min(height(i), height(j)) = min(8,7) = 7
   i             j                         AREA = 7*7 = 49
  
  In the End the max value of max_area will be printed
  
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i =0
        j = len(height)-1
        while i<j:
            max_area = max(max_area, (j-i)*min(height[i],height[j]))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            
        return max_area
        
