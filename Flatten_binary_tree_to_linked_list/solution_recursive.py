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
        #recursive
        if root is None:
            return
        left = root.left
        right = root.right
        #flatten left subtree and right subtree recursively
        self.flatten(left)
        self.flatten(right)
        #connect the flattend subtree
        if root.left:
            temp = root.right
            root.right = root.left
            root.left = None
            while root.right:
                root = root.right
            root.right = temp
        