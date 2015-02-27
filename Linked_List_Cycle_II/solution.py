#Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None or head.next is None: return None
        slow = head.next
        fast = head.next.next
        while slow!=fast:
            if fast is None or fast.next is None: return None
            else:
                slow = slow.next
                fast = fast.next.next
        fast = head
        while fast!=slow:
            fast = fast.next
            slow = slow.next
        return slow
        
