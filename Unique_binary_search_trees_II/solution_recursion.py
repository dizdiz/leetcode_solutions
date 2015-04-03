# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.helper(1,n)
        
    def helper(self, start, end):
        result = []
        if start>end:
            return [None]
        
        for i in range(start, end+1):
            leftsubtree = self.helper(start,i-1)
            rightsubtree = self.helper(i+1,end)
            for left in leftsubtree:
                for right in rightsubtree:
                    result.append(TreeNode(i))
                    result[-1].left = left
                    result[-1].right = right
        return result
            
        