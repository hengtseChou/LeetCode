class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        vowels = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        mask = 0
        max_len = 0
        hash_map = {0: -1}

        for i, char in enumerate(s):

            # If the same bitmask occurs at two different positions i and j,
            # it means that the substring between those two positions contains vowels in even counts.

            # The substring between i and j contains vowels with an even count
            # because the XOR of identical bitmasks is zero,
            # implying that the difference between them is zero.

            # We use a hash map to store the first occurrence of each bitmask.
            # As we traverse the string, we compute the bitmask for each index.
            # If that bitmask was seen before, it means the substring between the first occurrence
            # and the current position has even counts for all vowels.
            if char in vowels:
                mask ^= 1 << vowels[char]
            if mask in hash_map:
                max_len = max(max_len, i - hash_map[mask])
            else:
                hash_map[mask] = i

        return max_len
