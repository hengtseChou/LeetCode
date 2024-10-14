import heapq
from math import ceil


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        score = 0
        # try to hack a max heap by making nums negative
        nums = [num * -1 for num in nums]
        heapq.heapify(nums)
        for _ in range(k):
            max_val = heapq.heappop(nums) * -1
            score += max_val
            heapq.heappush(nums, ceil(max_val / 3) * -1)
        return score
