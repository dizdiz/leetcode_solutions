# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None or q is None:
            return q==p
        stackp = [p]
        stackq = [q]
        while stackp:
            node1 = stackp.pop()
            node2 = stackq.pop()
            if node1.val!=node2.val:
                return False
            if (node1.left is None and node2.left is not None) \
                or (node1.left is not None and node2.left is None)\
                or (node1.right is None and node2.right is not None) \
                or (node1.right is not None and node2.right is None):
                    return False
            if node1.left is not None:
                stackp.append(node1.left)
                stackq.append(node2.left)
            if node1.right is not None:
                stackp.append(node1.right)
                stackq.append(node2.right)
        return True
        