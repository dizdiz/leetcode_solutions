# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        #recursion
        res = []
        if root is None: return res
        left = self.inorderTraversal(root.left)
        res.extend(left)
        res.append(root.val)
        right = self.inorderTraversal(root.right)
        res.extend(right)
        return res
        