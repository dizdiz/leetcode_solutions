# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        l = []
        cur = []
        next = []
        if root is None:
            return l
        p = root
        l.insert(0,[p.val])
        cur.append(p)
        while cur:
            temp = []
            while cur:
                if cur[0].left:
                    temp.append(cur[0].left.val)
                    next.append(cur[0].left)
                if cur[0].right:
                    temp.append(cur[0].right.val)
                    next.append(cur[0].right)
                del cur[0]
            if temp:
                l.insert(0,temp)
            a = cur
            cur = next
            next = a
        return l