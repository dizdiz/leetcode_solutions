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
        #using Morris Traversal
        l = []
        cur = root
        while cur:
            if cur.left is None:
                l.append(cur.val)
                cur = cur.right
            else:
                #find predecessor of cur, which will be pre
                pre = cur.left
                while pre.right is not None and pre.right is not cur:
                    pre = pre.right
                if pre.right is None:
                    #thread pre in, and output cur.val
                    pre.right = cur
                    l.append(cur.val)
                    cur = cur.left
                else:
                    pre.right = None
                    cur = cur.right
        return l
                    
        