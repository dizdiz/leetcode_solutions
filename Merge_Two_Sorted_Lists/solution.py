# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        fakehead = ListNode(0)
        p1 = l1
        p2 = l2
        p = fakehead
        while p1!=None and p2!=None:
            if p1.val<=p2.val:
                p.next = p1
                p = p.next
                p1 = p1.next
            else:
                p.next = p2
                p = p.next
                p2 = p2.next
        if p1!=None:
            p.next = p1
        if p2!=None:
            p.next = p2
        return fakehead.next
