# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if len(lists)==0:
            return None
        return self.divide(lists,0,len(lists)-1)
        
    def divide(self,lists, start, end):
        if start>end:
            return None
        if start==end:
            return lists[start]
        mid = (start+end)/2
        l = self.divide(lists,start,mid)
        r = self.divide(lists, mid+1,end)
        return self.conquer(l,r)
    
    def conquer(self,l,r):
        fakehead = ListNode(0)
        f = fakehead
        while l is not None and r is not None:
            if l.val<r.val:
                f.next = l
                l = l.next
            else:
                f.next = r
                r = r.next
            f = f.next
        if l is None:
            f.next = r
        if r is None:
            f.next = l
        return fakehead.next
        