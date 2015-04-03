# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root is None:
            return
        fakehead = TreeNode(0)
        p = fakehead
        cur = root
        stack = []
        while cur or stack:
            while cur:
                if cur.right:
                    stack.append(cur.right)
                temp = cur
                cur = cur.left
                #set left and right node None
                temp.left = temp.right = None
                p.right = temp
                p = p.right
            if stack:
                cur = stack.pop()
        return
        