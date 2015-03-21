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
        #recursion
        l = []
        if root is None:
            return l
        l.extend(self.postorderTraversal(root.left))
        l.extend(self.postorderTraversal(root.right))
        l.append(root.val)
        return l
        