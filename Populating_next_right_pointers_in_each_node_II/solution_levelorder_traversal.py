# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        #level order traversal
        if root is None:
            return
        curq = []
        nextq = []
        curq.append(root)
        while curq:
            #next level enqueue(nextq)
            while curq:
                p = curq[0]
                del curq[0]
                if p.left:
                    nextq.append(p.left)
                if p.right:
                    nextq.append(p.right)
            #populating pointers
            index = 0
            while index<len(nextq)-1:
                nextq[index].next = nextq[index+1]
                index += 1
            #exchange reference, go down to next level
            temp = curq
            curq = nextq
            nextq = temp
        return
                
            