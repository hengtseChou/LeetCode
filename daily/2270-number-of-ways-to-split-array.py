class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        total = sum(nums)
        left_sum = 0
        ans = 0
        for num in nums[:-1]:
            left_sum += num
            if left_sum >= (total - left_sum):
                ans += 1
        return ans
