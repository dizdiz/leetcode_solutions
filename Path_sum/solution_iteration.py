# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        #iterative
        if root is None:
            return False
        stack = []
        cur = root
        temp = 0
        visited = None
        while cur or stack:
            while cur:
                stack.append(cur)
                temp += cur.val
                cur = cur.left
            cur = stack[-1]
            #if cur is leaf node,check the sum
            if cur.left is None and cur.right is None and temp==sum:
                return True
            if cur.right and cur.right is not visited:
                cur = cur.right
            else:
                temp = temp-cur.val
                stack.pop()
                visited = cur
                cur = None
        return False