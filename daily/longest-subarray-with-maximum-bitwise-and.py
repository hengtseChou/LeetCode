class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        ans = count = 1
        for i, num in enumerate(nums):

            if num == max_num:
                if i == 0:
                    continue
                elif nums[i] == nums[i - 1]:
                    count += 1
            else:
                ans = max(count, ans)
                count = 1

        ans = max(count, ans)
        return ans
