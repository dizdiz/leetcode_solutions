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
        #iteration, using stack
        stack = []
        l = []
        cur = root
        while cur is not None or len(stack)!=0:
            if cur is not None:
                l.append(cur.val);
                if cur.right is not None:
                    stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
        return l
        