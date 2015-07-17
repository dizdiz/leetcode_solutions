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
        l1 = self.preorderTraversal(root.left)
        l2 = self.preorderTraversal(root.right)
        l.extend(l1)
        l.extend(l2)
        return l
        