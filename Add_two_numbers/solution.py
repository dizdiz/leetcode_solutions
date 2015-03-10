# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        p1 = l1
        p2 = l2
        fakehead = ListNode(0)
        f = fakehead
        carry = 0
        while p1 is not None or p2 is not None:
            if p1 is not None and p2 is not None:
                sum = p1.val + p2.val + carry
                if sum>9:
                    f.next = ListNode(sum-10)
                    carry = 1
                else:
                    f.next = ListNode(sum)
                    carry = 0
                p1 = p1.next
                p2 = p2.next
            elif p1 is None:
                if (p2.val+carry)>9:
                    f.next = ListNode(0)
                    carry = 1
                else:
                    f.next = ListNode(p2.val+carry)
                    carry = 0
                p2 = p2.next
            else:
                if (p1.val+carry)>9:
                    f.next = ListNode(0)
                    carry = 1
                else:
                    f.next = ListNode(p1.val+carry)
                    carry = 0
                p1 = p1.next
            f = f.next
        return fakehead.next
                    
                
                
        