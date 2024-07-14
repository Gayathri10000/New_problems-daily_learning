# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def path(node, currpath, currsum):
            if not node:
                return 
            
            currpath.append(node.val) # the nodes will be stored
            currsum += node.val # the sum of the visited nodes

            if not node.left and not node.right:
                if targetSum == currsum: # check if equal to target or not 
                    ans.append(list(currpath))  # print the node in list 
            
            if node.left: #move to left tree
                path(node.left, currpath,currsum) 
                
            if node.right: # move to the right tree 
                path(node.right,currpath,currsum)

            currpath.pop() # backtracking 

        ans = []
        path(root,[],0) # calling the function
        return ans
