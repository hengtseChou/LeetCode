# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # was using id to check for identical node but not necessary
        # set is mutable and tuple is not mutable
        # The is operator checks whether two variables point to the exact same object in memory. 
        if head is None or head.next is None:
            return False

        nodes = set()

        while head.next is not None:
            head = head.next
            if head in nodes:
                return True
            else:
                nodes.add(head)                
            
        return False
        # 快慢指針法
        # slow = head
        # fast = head
        # while (slow is not None and fast is not None and fast.next is not None):
        #     slow = slow.next
        #     fast = fast.next.next
        #     if (slow == fast):
        #         return True
        # return False
        # O(1) (constant) memory
