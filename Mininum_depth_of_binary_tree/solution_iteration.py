# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root is None:
            return 0
        stack = []
        visited = None
        cur = root
        depth = 0
        mindepth = -1
        
        while cur or stack:
            while cur:
                stack.append(cur)
                depth += 1
                cur = cur.left
            cur = stack[-1]
            #when encounter a leaf node,check the minimum depth
            if cur.left is None and cur.right is None:
                if mindepth<0 or mindepth>depth:
                    mindepth = depth
            if cur.right and cur.right is not visited:
                cur = cur.right
            else:
                depth -= 1
                stack.pop()
                visited = cur
                cur = None
        return mindepth
            
        