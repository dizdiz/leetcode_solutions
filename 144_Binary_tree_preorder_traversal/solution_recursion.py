# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        #recursion
        l = []
        if root is None: return l
        l.append(root.val)
        l.extend(self.preorderTraversal(root.left))
        l.extend(self.preorderTraversal(root.right))
        return l
        