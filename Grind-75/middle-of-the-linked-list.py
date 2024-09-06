# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hash_map = {}
        count = 1
        while head:
            hash_map[count] = head
            count += 1
            head = head.next
        if count % 2 == 1:
            return hash_map[int((count + 1) / 2)]
        return hash_map[int(count / 2)]
