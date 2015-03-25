# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.helper(root,0)
    #
    def helper(self, node, path):
        if node is None:
            return 0
        path = path*10 + node.val
        if node.left is None and node.right is None:
            return path
        left = self.helper(node.left, path)
        right = self.helper(node.right, path)
        return left+right