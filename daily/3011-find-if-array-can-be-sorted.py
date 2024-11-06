class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_max = float("-inf")  # Tracks the maximum of the last group
        i = 0
        n = len(nums)

        while i < n:
            j = i + 1
            count = bin(nums[i]).count("1")  # Count of set bits for the current group
            current_min = current_max = nums[i]  # Initialize min and max for this group

            # Process all elements with the same count of set bits
            while j < n and bin(nums[j]).count("1") == count:
                current_min = min(current_min, nums[j])
                current_max = max(current_max, nums[j])
                j += 1  # Move to the next element

            # Check if the current group can be in order after the previous group
            if prev_max > current_min:
                return False  # Cannot be sorted under the given conditions

            prev_max = current_max  # Update prev_max for the next group
            i = j  # Move to the start of the next group

        return True
