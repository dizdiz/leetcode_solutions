# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        fakehead = ListNode(0)
        fakehead.next = head
        p = fakehead
        pre = fakehead
        cur = head
        while cur is not None:
            if cur.val<x:
                if p.next is not cur:
                    temp = p.next
                    p.next = cur
                    cur = cur.next
                    pre.next = cur
                    p = p.next
                    p.next = temp
                else:
                    cur = cur.next
                    pre = pre.next
                    p = p.next
            else:
                cur = cur.next
                pre = pre.next
        return fakehead.next
                
        