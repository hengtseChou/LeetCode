class Solution:
    def minEnd(self, n: int, x: int) -> int:

        # Initialize the result with the given x
        result = x
        remaining = n - 1
        position = 1

        while remaining:
            # Check if the current bit position in x is 0
            if not (x & position):
                # If the bit in x is 0, we may use this bit to make result larger
                # (remaining & 1) checks if the least significant bit of remaining is 1
                # If it is, we set the bit in result at 'position'
                result |= (remaining & 1) * position
                # Right shift 'remaining' to move to the next bit (divide by 2)
                remaining >>= 1
            # Move to the next bit position (double the value of position)
            position <<= 1

        return result
