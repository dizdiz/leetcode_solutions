# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        #This is merge sort!
        if head is None:
            return head
        if head is not None and head.next is None:
            return head
        #find middle
        mid = head
        tail = head
        while tail.next is not None and tail.next.next is not None:
            mid = mid.next
            tail = tail.next.next
        #recursion
        head1 = self.insertionSortList(mid.next)
        mid.next = None
        head2 = self.insertionSortList(head)
        #merge
        fakehead = ListNode(0)
        p = fakehead
        while head1 is not None and head2 is not None:
            if head1.val<head2.val:
                p.next = head1
                head1 = head1.next
            else:
                p.next = head2
                head2 = head2.next
            p = p.next
            p.next = None
        if head1 is not None:
            p.next = head1
        if head2 is not None:
            p.next = head2
        return fakehead.next
                
        
            
            
        