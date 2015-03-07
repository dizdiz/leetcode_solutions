# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        #if k is 1, no need to change the list
        if k==1:
            return head
        #calculate: how many group to be change 
        count = 0
        p = head
        while p is not None:
            p = p.next
            count += 1
        if count/k<1:
            return head
        #reverse list by group in for loop
        fakehead = ListNode(0)
        tail = fakehead
        p1 = head
        for i in range(0,count/k):
            m = k
            #change one group
            while m>0:
                m -= 1
                p2 = tail.next
                temp = p1
                p1 = p1.next
                temp.next = p2
                tail.next = temp
            #one group is reversed, move tail to the end
            #to reverse the next group
            while tail.next is not None:
                tail = tail.next
        #connect the remaining nodes
        tail.next = p1
        return fakehead.next
            
        