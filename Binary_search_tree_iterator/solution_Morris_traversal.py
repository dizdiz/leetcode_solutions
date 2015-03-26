# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.cur = root
        
        
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.cur:
            return True
        return False
       

    # @return an integer, the next smallest number
    def next(self):
        #Morris Traversal, no stack needed
        while self.cur:
            if self.cur.left is None:
                result = self.cur.val
                self.cur = self.cur.right
                break
            else:
                pre = self.cur.left
                while pre.right is not None and pre.right is not self.cur:
                    pre = pre.right
                if pre.right is None:
                    pre.right = self.cur
                    self.cur = self.cur.left
                else:
                    pre.right = None
                    result = self.cur.val
                    self.cur = self.cur.right
                    break
        return result

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())