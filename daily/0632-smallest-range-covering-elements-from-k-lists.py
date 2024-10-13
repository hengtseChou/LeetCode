import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        # 1. merge k sorted array + minimum sliding window
        # merged = []
        # for i in range(len(nums)):
        #     for num in nums[i]:
        #         merged.append((num, i))  # (value, list index)

        # merged.sort()

        # # Sliding window variables
        # count = defaultdict(int)  # To count how many elements we have from each list in the window
        # unique_list_count = 0  # How many unique lists are currently represented in the window
        # left = 0  # Left pointer of the window
        # min_range = [-float('inf'), float('inf')]  # The best range we found

        # for right in range(len(merged)):
        #     num, list_idx = merged[right]

        #     # Add the current element to the window
        #     count[list_idx] += 1
        #     if count[list_idx] == 1:
        #         unique_list_count += 1  # New list is represented in the window

        #     # When we have at least one element from each list, try to shrink the window
        #     while unique_list_count == len(nums):
        #         current_range = merged[right][0] - merged[left][0]
        #         # Update the best range if the current one is smaller
        #         if current_range < min_range[1] - min_range[0]:
        #             min_range = [merged[left][0], merged[right][0]]

        #         # Shrink the window from the left
        #         left_num, left_list_idx = merged[left]
        #         count[left_list_idx] -= 1
        #         if count[left_list_idx] == 0:
        #             unique_list_count -= 1  # We lost one list representation in the window
        #         left += 1

        # return min_range

        # 2. min heap
        # this has a better memory usage
        import heapq

        min_heap = []
        max_value = float("-inf")

        # Initialize the heap with the first element of each list along with the list index and element index
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0])

        # Track the best (smallest) range
        best_range = [-float("inf"), float("inf")]

        # Process the heap
        while min_heap:
            min_value, list_idx, ele_idx = heapq.heappop(min_heap)

            # Update the best range if the current one is smaller
            if max_value - min_value < best_range[1] - best_range[0]:
                best_range = [min_value, max_value]

            # If the current list is exhausted, stop
            if ele_idx + 1 == len(nums[list_idx]):
                break

            # Add the next element from the same list to the heap
            next_value = nums[list_idx][ele_idx + 1]
            heapq.heappush(min_heap, (next_value, list_idx, ele_idx + 1))

            # Update the maximum value
            max_value = max(max_value, next_value)

        return best_range
