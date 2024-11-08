class Solution:
    def sortColors(self, nums: List[int]) -> None:

        # 3 pointers
        # ref: https://leetcode.com/problems/sort-colors/solutions/5580767/video-2-solutions-with-frequency-or-3-pointers

        red = 0
        white = 0
        blue = len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
