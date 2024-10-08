class Solution:
    def minSwaps(self, s: str) -> int:

        # ref: https://algo.monster/liteproblems/1963

        ans = 0  # Keeps track of unmatched opening brackets '['

        # Iterate through each character in the string
        for c in s:
            if c == "[":
                ans += 1  # Increment for each unmatched opening bracket '['
            elif ans:
                ans -= 1  # Decrement when a closing bracket ']' matches with an existing opening bracket '['

        # Return the minimum number of swaps needed
        # (ans + 1) >> 1 is a bit-shifting trick that efficiently computes the ceiling of half the number of unmatched brackets.
        # For example, if there are 3 unmatched opening brackets, it will return 2 swaps (since each swap can resolve two unmatched brackets).
        return (ans + 1) >> 1
