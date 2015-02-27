# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head is None: return None
        fakehead = ListNode(0)
        fakehead.next = head
        pre = fakehead
        end = head
        p = head
        #find out which one to remove
        for i in range(1,n):
            end = end.next
        while end.next!=None:
            end = end.next
            p = p.next
            pre = pre.next
        #remove node p
        pre.next = p.next
        del p
        return fakehead.next
        
        
            
            
        
