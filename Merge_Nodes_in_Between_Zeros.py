# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        sum = 0
        prev , curr = head, head.next
        while curr:
            node = curr.val
            if node != 0:
                sum += node
            else:
                prev.next = ListNode(sum) 
                # Creates the new node that holds the sum links to prev node
                prev = prev.next
                sum = 0
            curr = curr.next
        return head.next     
        
