# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True
        left = self.findDepth(root.left)
        right = self.findDepth(root.right)
        if abs(left-right)>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def findDepth(self,node):
        if node is None:
            return 0
        left = self.findDepth(node.left)+1
        right = self.findDepth(node.right)+1
        return max(left,right)