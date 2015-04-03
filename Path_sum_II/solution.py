# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        #dfs
        if root is None:
            return []
        stack = []
        l = []
        result = []
        cur = root
        visited = None
        temp = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                l.append(cur.val)
                temp = temp + cur.val
                cur = cur.left
            cur = stack[-1]
            if cur.left is None and cur.right is None and temp==sum:
                a = []
                a.extend(l)
                result.insert(len(result),a)
            if cur.right and cur.right is not visited:
                cur = cur.right
            else:
                temp = temp - cur.val
                stack.pop()
                l.pop()
                visited = cur
                cur = None
        return result