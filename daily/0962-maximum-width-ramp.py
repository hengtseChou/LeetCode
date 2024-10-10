class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        # ref: https://algo.monster/liteproblems/962

        stack = []
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        max_width = 0
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                max_width = max(max_width, j - i)

        return max_width
