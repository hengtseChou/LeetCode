# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # just check if root1 and root2 have the same children for every node.
        if root1 is None and root2 is None:
            return True
        if (root1 is None and root2 is not None) or (root2 is None and root1 is not None):
            return False
        if root1.val != root2.val:
            return False
        hash_map1 = {}
        hash_map2 = {}

        queue1 = deque([root1])
        queue2 = deque([root2])

        while queue1:

            node = queue1.popleft()
            left = node.left.val if node.left else None
            right = node.right.val if node.right else None

            hash_map1[node.val] = {left, right}

            if node.left:
                queue1.append(node.left)
            if node.right:
                queue1.append(node.right)

        while queue2:

            node = queue2.popleft()
            left = node.left.val if node.left else None
            right = node.right.val if node.right else None

            hash_map2[node.val] = {left, right}

            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)

        if len(hash_map1) != len(hash_map2):
            return False

        for key in hash_map1.keys():
            if hash_map1[key] != hash_map2[key]:
                return False

        return True

    # standard solution
    # def flipEquiv(self, root1, root2):

    #     def checker(node1, node2):
    #         if not node1 and not node2:
    #             return True
    #         if not node1 or not node2 or node1.val != node2.val:
    #             return False
    #         return ((checker(node1.left, node2.left) or checker(node1.left, node2.right)) and
    #                 (checker(node1.right, node2.right) or checker(node1.right, node2.left)))

    #     return checker(root1, root2)
