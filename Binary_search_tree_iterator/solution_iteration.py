# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        #using inorder traversal,
        #construct a sorted list which contains all the value of the tree 
        stack = []
        self.l = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            self.l.append(cur.val)
            cur = cur.right
        
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        #to see if the sorted list has values in it or not
        if self.l:
            return True
        return False

    # @return an integer, the next smallest number
    def next(self):
        #return the head of the sorted list and delete it
        n = self.l[0]
        del self.l[0]
        return n

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())