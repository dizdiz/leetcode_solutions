# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        if head is None: return None
        elif head.next is None:
            treenode = TreeNode(head.val)
            return treenode
        else:
            middle = head
            end = head
            fakehead = ListNode(0)
            fakehead.next = head
            pre = fakehead
            while end is not None and end.next is not None:
                pre = pre.next
                middle = middle.next
                end = end.next.next
            root = TreeNode(middle.val)
            root.right = self.sortedListToBST(middle.next)
            pre.next = None
            root.left = self.sortedListToBST(head)
            return root
        
