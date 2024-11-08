class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        max_value = (1 << maximumBit) - 1  # This is equivalent to 2^maximumBit - 1

        # Calculate the cumulative XOR of the entire array
        xor = 0
        for num in nums:
            xor ^= num

        result = []
        # Process each query in reverse order
        for _ in range(len(nums)):
            # Find x such that xor ^ x is maximized
            x = max_value ^ xor
            result.append(x)
            # Remove the last element from nums and update the cumulative xor
            xor ^= nums.pop()

        return result
