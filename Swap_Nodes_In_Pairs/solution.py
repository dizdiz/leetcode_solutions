#Given a linked list, swap every two adjacent nodes and return its head.

#For example,
#Given 1->2->3->4, you should return the list as 2->1->4->3.

#Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        fakehead = ListNode(0)
        fakehead.next = head
        p = head
        pre = fakehead
        
        while p!=None:
            if p.next!=None:
                temp = p.next.next
                pre.next = p.next
                pre = pre.next
                pre.next = p
                pre = pre.next
                p.next = temp
                p = p.next
            else:
                break
        return fakehead.next
