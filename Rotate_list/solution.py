# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head is None:
            return head
        if k is 0:
             return head
        fakehead = ListNode(0)
        fakehead.next = head
        pre = tail = fakehead
        p = head
        count = 0
        #calculate the length of the list and find the tail of the list
        while p is not None:
            p = p.next
            tail = tail.next
            count += 1
        #find where the rotate starts
        if k%count==0:
            return head
        count = count - (k % count)
        p = head
        while count>0:
            count -= 1
            pre = pre.next
            p = p.next
        #start rotating (insert everything starting from p after fakehead, and connect it with head)
        fakehead.next = p
        tail.next = head
        pre.next = None
        return fakehead.next
        
        
        
        
        