# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Euclidean Algorithm
    def gcd(self, a, b):
        if a == 0:
            return b

        return gcd(b % a, a)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = head
        while dummy.next is not None:
            new_node = ListNode(val=self.gcd(dummy.val, dummy.next.val), next=dummy.next)
            dummy.next = new_node
            dummy = dummy.next.next
        return head
