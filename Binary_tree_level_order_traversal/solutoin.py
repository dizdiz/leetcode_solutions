# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None:
            return []
        res = []
        l = []
        q1 = []
        q2 = []
        q1.append(root)

        while q1:
            p = q1[0]
            #l stores the value of the entire level temporarily
            l.append(p.val)
            if p.left:
                q2.append(p.left)
            if p.right:
                q2.append(p.right)
            del q1[0]
            #one level is traversed, insert l in  result, then empty l
            #q1 and q2 exchange
            if len(q1)==0:
                res.insert(len(res),l)
                l = []
                temp = q1
                q1 = q2
                q2 = temp
        return res
        
        