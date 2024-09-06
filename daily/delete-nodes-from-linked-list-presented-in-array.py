# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        s = set(nums)
        # use a dummy head and a curr pointer to traverse through the nodes
        # dummy's next will always point at the original head
        # while curr can jump or move to the next one
        dummy = curr = ListNode(next=head)
        while curr.next:
            if curr.next.val in s:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next
