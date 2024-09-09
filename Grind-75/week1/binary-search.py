class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while (left <= right):
            
            mid = (left + right) // 2
            if (nums[mid] > target):
                # dropping upper half
                right = mid - 1
            elif (nums[mid] < target):
                # dropping lower half
                left = mid + 1
            else:
                return mid

        return -1
