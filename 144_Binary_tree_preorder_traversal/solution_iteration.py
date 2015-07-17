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
        #iteration, using stack(push right nodes)
        stack = []
        l = []
        cur = root
        while cur or stack:
            while cur:
                l.append(cur.val);
                if cur.right:
                    stack.append(cur.right)
                cur = cur.left
            if stack:
                cur = stack.pop()
        return l
        