# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder)==0:
            return None
        return self.helper(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
    def helper(self,preorder,pstart,pend,inorder,istart,iend):
        if pstart>pend:
            return None
        if pstart == pend:
            return TreeNode(preorder[pstart])
        root = TreeNode(preorder[pstart])
        middle = istart
        while inorder[middle]!=root.val:
            middle += 1
        root.left = self.helper(preorder,pstart+1,pstart+middle-istart, inorder, istart, middle-1)
        root.right = self.helper(preorder,pstart+middle-istart+1,pend,inorder,middle+1,iend)
        return root