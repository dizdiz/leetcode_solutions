# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        #using merge sort
        if head is None:
            return head
        if head is not None and head.next is None:
            return head
        #divide(find middle)
        mid = tail = head
        while tail.next is not None and tail.next.next is not None:
            mid = mid.next
            tail = tail.next.next
        l1 = self.sortList(mid.next)
        mid.next = None
        l2 = self.sortList(head)
        #merge
        fakehead = ListNode(0)
        f = fakehead
        while l1 is not None and l2 is not None:
            if l1.val<l2.val:
                f.next = l1
                l1 = l1.next
            else:
                f.next = l2
                l2 = l2.next
            f = f.next
            f.next = None
        if l1 is None and l2 is not None:
            f.next = l2
        if l1 is not None and l2 is None:
            f.next = l1
        return fakehead.next
        
        