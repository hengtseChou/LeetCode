# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 1st attempt
        # if head is None:
        #     return None
        # tail_created = False
        # while head != None:
        #     if not tail_created:
        #         rev = ListNode(val = head.val)
        #         head = head.next
        #         tail_created = True
        #     else:
        #         rev = ListNode(val=head.val, next=rev)
        #         head = head.next
        # return rev

        # 2nd attempt
        # less speedy but memory efficient
        # init with prev, curr and next
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
