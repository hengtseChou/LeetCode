class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        ans = 0
        # 10^7 will take 24 bits only
        for i in range(24):
            # checks whether the i-th bit of candidate is set (i.e., is 1).
            count = sum(1 for candidate in candidates if candidate & (1 << i))
            ans = max(count, ans)
        return ans
