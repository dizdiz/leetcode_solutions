# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None:
            return head
        fakehead = ListNode(0)
        fakehead.next = head
        pre = fakehead
        cur = head
        
        while True:
            if cur is None:
                return fakehead.next
            if cur.next is None:
                return fakehead.next
            if cur.val!=cur.next.val:
                pre = pre.next
                cur = cur.next
            else:
                while cur.next is not None and cur.val==cur.next.val:
                    temp = cur
                    cur = cur.next
                    del temp
                temp = cur
                cur = cur.next
                del temp
                pre.next = cur
        return fakehead.next
        
        comment_block='''
        while cur is not None and cur.next is not None:
            if cur.val==cur.next.val:
                val = cur.val
                while cur is not None and cur.val==val:
                    temp = cur
                    cur = cur.next
                    del temp
                pre.next = cur
            else:
                pre = pre.next
                cur = cur.next
        return fakehead.next
        '''
        
        
                