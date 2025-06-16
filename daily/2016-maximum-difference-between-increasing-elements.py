class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # similar to best time to buy and sell stock
        # so we keep track of the minimum number
        # and compare the diff to max_diff once a larger value occurs
        min_num = 10**9 + 1
        max_diff = -1
        for num in nums:
            if num <= min_num:
                min_num = num
            else:
                max_diff = max(max_diff, num - min_num)
        return max_diff
