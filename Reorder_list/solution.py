# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head is None:
            return
        if head is not None and head.next is None:
            return
        #find the last half(starts with head2)
        mid = tail = head
        while tail.next is not None and tail.next.next is not None:
            mid = mid.next
            tail = tail.next.next
        head2 = mid.next
        mid.next = None
        #reverse the last half
        fakehead = ListNode(0)
        while head2 is not None:
            temp = head2
            head2 = head2.next
            temp.next = fakehead.next
            fakehead.next = temp
        #interleave head and head2
        p = head
        f = fakehead.next
        while f is not None:
            temp = f
            f = f.next
            temp.next = p.next
            p.next = temp
            p = temp.next
        return
            
        