# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        #Morris Traversal
        l = []
        cur = root
        while cur:
            if cur.left is None:
                l.append(cur.val)
                cur = cur.right
            else:
                #find predecessor in cur's left subtree, and thread
                pre = cur.left
                while pre.right is not None and pre.right is not cur:
                    pre = pre.right
                #thread, cur move to left(continue threading)
                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                else:
                    #revert the change(undo the threading)
                    #cur can now be put into list
                    #goto cur's right
                    pre.right = None
                    l.append(cur.val)
                    cur = cur.right
        return l
                