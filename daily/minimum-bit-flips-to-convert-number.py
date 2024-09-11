class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        t = start ^ goal
        # The result t is an integer where the set bits (i.e., bits that are 1)
        # represent positions where start and goal have different bits, which would need to be flipped.
        ans = 0
        while t:
            ans += t & 1
            t >>= 1
            # t & 1 checks if the least significant bit (LSB) of t is 1.
            # If it is, it adds 1 to ans, counting this as a bit flip.
            # t >>= 1 shifts t one bit to the right,
            # essentially moving to the next bit for the next iteration.
            # In conclusion: compare bits starts from the least significant bit and count, thats it
        return ans
