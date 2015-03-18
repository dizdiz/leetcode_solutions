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
        if root is None:
            return 0
        level = 0    
        cur_level = []
        next_level = []
        cur_level.append(root)
        while len(cur_level) is not 0:
            if cur_level[0].left is not None:
                next_level.append(cur_level[0].left)
            if cur_level[0].right is not None:
                next_level.append(cur_level[0].right)
            del cur_level[0]
            if len(cur_level)==0:
                temp = cur_level
                cur_level = next_level
                next_level = temp
                level += 1
        return level
                
        
        
            
        