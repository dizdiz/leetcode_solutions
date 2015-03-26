# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        #recursive
        if root is None:
            return False
        if root.left is None and root.right is None and root.val==sum:
            return True
        sum = sum-root.val
        left = right = False
        left = self.hasPathSum(root.left,sum)
        right = self.hasPathSum(root.right,sum)
        return left or right
        