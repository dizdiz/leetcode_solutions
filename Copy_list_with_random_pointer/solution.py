# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head is None:
            return head
        
        #generate new list nodes and interleave them with the oldlist
        p = head
        while p is not None:
            temp = RandomListNode(p.label)
            temp.next = p.next
            p.next = temp
            p = temp.next
        #copy random pointer
        p = head
        while p is not None:
            if p.random is None:
                p.next.random = None
            else:
                p.next.random = p.random.next
            p = p.next.next
        #extract new list
        f = fakehead = RandomListNode(0)
        p = head
        while p is not None:
            temp = p.next
            p.next = temp.next
            p = p.next
            temp.next = None
            f.next = temp
            f = f.next
        return fakehead.next
        #solution using dict, key is new nodes.a little slower
        comm = '''
        dic = dict()
        m = n = head
        #create nodes in dict, key is oldnodes, value is newnodes
        while m:
            dic[m] = RandomListNode(m.label)
            m = m.next
        #for every key(new nodes), copy pointers using 'get' method
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)
        '''
            