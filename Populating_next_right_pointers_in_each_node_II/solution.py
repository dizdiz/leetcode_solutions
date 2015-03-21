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
        if root is None:
            return
        p = root
        if p.left:
            head = p.left
        elif p.right:
            head = p.right
        else:
            return
        fakehead = TreeNode(0)
        pre = fakehead
        while head:
            #populating next level
            while p:
                if p.left:
                    pre.next = p.left
                    pre = pre.next
                if p.right:
                    pre.next = p.right
                    pre = pre.next
                p = p.next
            #reset pre to populate next level
            pre = fakehead
            #find head of next level
            head = None
            temp = fakehead.next
            while temp:
                if temp.left:
                    head = temp.left
                    break
                if temp.right:
                    head = temp.right
                    break
                temp = temp.next
            #p points to head of the connected level
            p = fakehead.next
        return