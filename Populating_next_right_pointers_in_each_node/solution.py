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
        fakehead = TreeNode(0)
        pre = fakehead
        while p.left:
            while p:
                pre.next = p.left
                p.left.next = p.right
                pre = p.right
                p = p.next
            #reset pre to prepare to populate next level
            pre = fakehead
            #p points to the head of the connected level
            p = fakehead.next
        return