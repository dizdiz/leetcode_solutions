# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.judge(root.left,root.right)
    
    def judge(self,left,right):
        if left is None or right is None:
            return left==right
        if left.val!=right.val:
            return False
        a = self.judge(left.left,right.right)
        b = self.judge(left.right,right.left)
        return a and b