# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def leafs(node,num):
            if not node:
                return 0
            
            num = num*10 + node.val
          ''' above code line process is 
                The root-to-leaf path 4->9->5 represents the number 495 
                    initially the num = 0 then 
                    the starting nodes is 4 so, num = 0 *10 + 4 is 4
                    the next node is 9 then, num =4*10+9 is 49
                    the next node is 5 then, num = 49 * 10 + 5 is 495
           '''

            if not node.left and not node.right:
                return num
            
            l_s = leafs(node.left,num)
            r_s = leafs(node.right,num)
            return l_s + r_s

        return leafs(root,0)
