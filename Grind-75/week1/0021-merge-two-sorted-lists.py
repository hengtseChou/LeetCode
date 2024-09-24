# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # list1 and list2 are the heads of the two ListNode
        dummy = ListNode(0)
        tail = dummy

        while True:

            if list1 is None:
                tail.next = list2
                break
            if list2 is None:
                tail.next = list1
                break
            
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # print(tail)
            tail = tail.next
            # print(tail)
            # print("---")
        return dummy.next
