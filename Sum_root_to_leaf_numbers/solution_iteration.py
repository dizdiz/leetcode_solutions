# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root is None:
            return 0
        results = []
        stack = []
        temp = 0
        visited = None
        cur = root
        #DFS traversal, 
        #when there's a leafnode, the stack has the way this node to root
        while cur or stack:
            while cur is not None:
                stack.append(cur)
                temp = temp*10 + cur.val
                cur = cur.left
            cur = stack[-1]
            
            #if cur is a leafnode, push the sum into stack
            if cur.left is None and cur.right is None:
                results.append(temp)
            
            if cur.right and cur.right is not visited:
                cur = cur.right
            else:
                temp = temp/10
                stack.pop()
                visited = cur
                cur = None
        res = 0
        for i in results:
            res = res+i
        return res
            