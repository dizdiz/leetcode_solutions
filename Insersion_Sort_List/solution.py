# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        #move every element after head to fakehead
        fakehead = ListNode(0)
        cur = head
        while cur is not None:
            p1 = fakehead
            p2 = fakehead.next
            #find insersion place: p1-cur-p2
            while p2 is not None and p2.val<cur.val:
                p1 = p1.next
                p2 = p2.next
            p1.next = cur
            cur = cur.next
            p1 = p1.next
            p1.next = p2
        return fakehead.next
            
            
        