# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder)==0:
            return None
        return self.helper(inorder, 0, len(inorder)-1, postorder, 0,len(postorder)-1)
    def helper(self, inorder, istart,iend,postorder,pstart,pend):
        if istart>iend:
            return None
        if istart==iend:
            return TreeNode(inorder[istart])
        root = TreeNode(postorder[pend])
        middle = istart
        while inorder[middle]!=root.val:
            middle += 1
        #the offset of pend should be calculated from middle&istart
        root.left = self.helper(inorder, istart, middle-1, postorder, pstart,pstart+(middle-istart-1))
        #the offset of pstart should be calculated from middle&istart
        root.right = self.helper(inorder, middle+1, iend, postorder, pstart+middle-istart, pend-1)
        return root
        