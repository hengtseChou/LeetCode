# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # ref: https://www.geeksforgeeks.org/check-if-all-elements-of-given-linked-list-corresponds-to-a-downward-path-from-any-node-in-given-binary-tree/
    def traverse(self, curr_head, curr_tree):

        if curr_head is None:
            return True
        if curr_tree is None:
            return False
        if curr_head.val == curr_tree.val:
            return self.traverse(curr_head.next, curr_tree.left) or self.traverse(curr_head.next, curr_tree.right)
        return False

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        if head is None:
            return True # the linked list has completed
        if root is None:
            return False # the tree node does not exist

        is_sub_path = False
        if head.val == root.val:
            # check the next node by the left or right child
            is_sub_path = self.traverse(head.next, root.left) or self.traverse(head.next, root.right)
        # if the current node does not make a sub path, check for left or right child
        return is_sub_path or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
