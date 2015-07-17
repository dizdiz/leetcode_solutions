# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def reorder(self, start, end):
        #reverse the nodes from node 'start' to nod 'end'
        #notice: in this situation,every node is its parent node's right child
        if start==end:
            return
        x = start
        y = start.right
        while x is not end:
            z = y.right
            y.right = x
            x = y
            y = z
        return

    def postorderTraversal(self, root):
        #Morris Traversal
        l = []
        if root is None:
            return l
        fakeroot = TreeNode(0)
        fakeroot.left = root
        cur = fakeroot
        
        while cur:
            if cur.left is None:
                cur = cur.right
            else:
                #find cur's predecessor in inorder traversal, which will be pre
                pre = cur.left
                while pre.right is not None and pre.right is not cur:
                    pre = pre.right
                #if pre isn't threaded, thread it , cur goes to left child
                if pre.right is None:
                    pre.right = cur
                    cur = cur.left
                #if pre is threaded, then reverse the nodes from cur's left child to pre, out put.
                else:
                    start = cur.left
                    end = pre
                    #reversing output
                    self.reorder(start, end)
                    p = end
                    while p is not start:
                        l.append(p.val)
                        p = p.right
                    l.append(start.val)
                    #reverse back, keep the tree unchanged   
                    self.reorder(end, start)
                    #un-thread pre, cur goes to right child
                    pre.right = None
                    cur = cur.right
        return l