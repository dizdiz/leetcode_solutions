# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        stack = []
        visited = None
        cur = root
        max_depth = 0
        while cur is not None or len(stack)!=0:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            stack.append(cur)
            if cur.left is None and cur.right is None:
                if max_depth<(len(stack)):
                    max_depth = len(stack)
            if cur.right is not None and cur.right is not visited:
                cur = cur.right
            else:
                stack.pop()
                visited = cur
                cur = None
        return max_depth
            
        