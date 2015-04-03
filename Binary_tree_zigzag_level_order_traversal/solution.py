# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        result = []
        temp = []
        cur = []
        next = []
        check = 1
        cur.append(root)
        while cur:
            p = cur[0]
            temp.append(p.val)
            if p.left:
                next.append(p.left)
            if p.right:
                next.append(p.right)
            del cur[0]
            if len(cur)==0:
                if check%2==0:
                    temp.reverse()
                check += 1
                result.append(temp)
                temp = []
                l = cur
                cur = next
                next = l
        return result
                
                    