class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        # there is also another solution using sorted nums and hashmap

        max_streak = -1
        arr = [0] * 100001  # because 317 * 317 > 100000, it suffices to loop only these values
        for num in nums:
            arr[num] = 1
        for i in range(2, 317):
            if arr[i] == 0:
                continue
            curr = i
            curr_streak = 0
            while curr <= 100000 and arr[curr] == 1:
                arr[curr] = 0  # Mark as visited to avoid cycles
                curr *= curr
                curr_streak += 1
            max_streak = max(max_streak, curr_streak)

        return max_streak if max_streak > 1 else -1
