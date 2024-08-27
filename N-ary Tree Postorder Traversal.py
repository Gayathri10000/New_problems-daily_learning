"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root: #check root
            return []
        res =[]
        def dfs(root): 
            for x in root.children: #traversal through the node
                dfs(x)
            res.append(root.val) # add root node to the res list in postorder
        dfs(root)
        return res # return the return
