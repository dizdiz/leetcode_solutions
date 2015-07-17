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
        #iteration, using DFS(push whatever encountered into stack)
        stack = []
        l = []
        cur = root
        while cur is not None or len(stack)!=0:
            while cur is not None:
                stack.append(cur)
                l.append(cur.val)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return l
            
                    
        