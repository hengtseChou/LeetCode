# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary search
        left = 1
        right = n        
        while (left <= right):
            mid = (left + right) // 2
            if isBadVersion(mid):
                # terminal condition
                # should carefully think about this part
                if mid == 1 or not isBadVersion(mid - 1):
                    return mid
                right = mid - 1
            else:
                left = mid + 1
                
        return None
