# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None: return None
        sizeA = 0
        sizeB = 0
        pa = headA
        pb = headB
        #calculate size
        while pa is not None:
            sizeA += 1
            pa = pa.next
        while pb is not None:
            sizeB += 1
            pb = pb.next
        #put pa and pb in the same position, then start to see if they intersected
        pa = headA
        pb = headB
        if sizeA>sizeB:
            for i in range(0,sizeA-sizeB):
                pa = pa.next
        else:
            for i in range(0,sizeB-sizeA):
                pb = pb.next
        while pa is not None and pb is not None:
            if pa==pb :
                return pb
            pa = pa.next
            pb = pb.next
        return None
        
        
