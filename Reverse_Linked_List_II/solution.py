# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        fakehead = ListNode(0)
        fakehead.next = head
        pre = fakehead
        cur = head
        i = 1
        #find the start place
        while i<m:
            cur = cur.next
            pre = pre.next
            i += 1
        flag = pre
        #start reversing, the reversed part is after reverse_head
        reverse_head = ListNode(0)
        while i<=n:
            r = reverse_head
            temp = r.next
            reverse_head.next = cur
            cur = cur.next
            pre.next = cur
            r = r.next
            r.next = temp
            i += 1
        r = reverse_head
        while r.next is not None:
            r = r.next
        flag.next = reverse_head.next
        r.next = cur
        return fakehead.next
        
            
            
            
        
            
            
        
        