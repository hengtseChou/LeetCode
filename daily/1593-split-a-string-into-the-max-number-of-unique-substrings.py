class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, used_substrings):
            # If we have processed the entire string, return 0 as there are no more substrings to add
            if start == len(s):
                return 0

            max_splits = 0  # To store the maximum number of splits

            # Try to take every possible substring starting from the index 'start'
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                # Only proceed if this substring is unique
                if substring not in used_substrings:
                    used_substrings.add(substring)  # Add this substring to the set
                    # Recur for the remaining string and count the current split
                    max_splits = max(max_splits, 1 + backtrack(end, used_substrings))
                    used_substrings.remove(
                        substring
                    )  # Backtrack by removing the last added substring

            return max_splits

        # Call the backtracking helper starting from index 0 and an empty set for used substrings
        return backtrack(0, set())
