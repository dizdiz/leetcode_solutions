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
        return self.helper(root,sum, 0)
    #add node value from top to bottom, 
    #until there's a value that equals the given sum
    def helper(self, node, sum, path_sum):
        res = False
        if node is None:
            return res or False
        if node.left is None and node.right is None:
            if node.val+ path_sum == sum:
                return res or True
            else:
                return res or False
        left = right = False
        if node.left:
            left =  res or self.helper(node.left, sum, path_sum+node.val)
        if node.right:
            right = res or self.helper(node.right, sum, path_sum+node.val)
        return left or right
        