# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        #recursive
        l = []
        stack = []
        if root is None:
            return l
        cur = root
        visited = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack[-1]
            if cur.right and cur.right is not visited:
                cur = cur.right
            else:
                l.append(cur.val)
                stack.pop()
                visited = cur
                cur = None
        return l