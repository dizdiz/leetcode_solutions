# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left and root.right is None:
            return 1+self.minDepth(root.left)
        if root.right and root.left is None:
            return 1+self.minDepth(root.right)
        if root.left and root.right:
            left = 1+self.minDepth(root.left)
            right = 1+self.minDepth(root.right)
            return min(left,right)
            
        