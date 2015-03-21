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
        #traversal the tree, for every node, 
        #keep track of its depth in a stack(depth)

        m_depth = 0
        cur_depth = 0
        cur = root
        stack = []
        depth = []
        while cur or stack:
            #traversal the tree in preorder
            #find out the depth of every node
            if cur is not None:
                cur_depth += 1
                if cur.right is not None:
                    stack.append(cur.right)
                    depth.append(cur_depth)
                cur = cur.left
            else:
                cur = stack.pop()
                cur_depth = depth.pop()
            
            #whenever cur_depth changes, 
            #compare it with maximum depth to see 
            #if we need to update maximum depth
            if cur_depth>m_depth:
                m_depth = cur_depth
        return m_depth
        