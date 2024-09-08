# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        count = 0
        hash_table = {}
        dummy = head
        while dummy is not None:
            count += 1
            hash_table[count] = dummy
            dummy = dummy.next

        if count < k:
            count_each = [1] * count + [0] * (k - count)
        else:
            remainder = count % k
            count_each = [(count // k) + 1] * remainder + [(count // k)] * (k - remainder)

        output = [None] * k
        idx = 1
        for i, count in enumerate(count_each):
            if count == 0:
                continue
            new_head = ListNode(next=hash_table[idx])
            dummy = new_head
            for _ in range(count):
                dummy = dummy.next
            dummy.next = None
            idx += count
            output[i] = new_head.next

        return output
