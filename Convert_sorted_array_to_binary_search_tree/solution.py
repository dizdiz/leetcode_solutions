# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num)==0:
            return None
        root = self.helper(num,0,len(num)-1)
        return root
    def helper(self,num,start,end):
        mid = (start+end)/2
        root = TreeNode(num[mid])
        if start!=mid:
            root.left = self.helper(num,start,mid-1)
        if end!=start:
            root.right = self.helper(num,mid+1,end)
        return root
        
        