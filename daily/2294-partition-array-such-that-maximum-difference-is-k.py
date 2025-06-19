class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        ans = 1
        nums.sort()
        current_min = nums[0]
        for num in nums[1:]:
            if num - current_min > k:
                ans += 1
                current_min = num
        return ans
