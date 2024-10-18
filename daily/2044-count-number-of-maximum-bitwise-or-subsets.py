class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Step 1: Find the maximum bitwise OR achievable
        max_or = 0
        for num in nums:
            max_or |= num  # OR all the numbers together to find the maximum possible OR

        # Step 2: Initialize a counter for subsets with max OR
        count = 0

        # Step 3: Backtracking function to explore all subsets
        def backtrack(i, current_or):
            nonlocal count
            # Base case: if we've considered all elements
            if i == len(nums):
                if current_or == max_or:  # If current OR equals the max OR, count this subset
                    count += 1
                return

            # Recursive case: we either include nums[i] in the subset or we don't
            # 1. Include nums[i]
            backtrack(i + 1, current_or | nums[i])
            # 2. Exclude nums[i]
            backtrack(i + 1, current_or)

        # Step 4: Start backtracking from the 0th index with initial OR of 0
        backtrack(0, 0)

        return count
