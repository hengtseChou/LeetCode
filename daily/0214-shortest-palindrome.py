class Solution:
    def shortestPalindrome(self, s: str) -> str:

        # rolling hashing algorithm
        # when comparing substrings, we are comparing each characters
        # and if we use hashing, the comparison is O(n) complexity

        n = len(s)
        if n == 0:
            return s
        MOD = 10**9 + 7
        BASE = 31

        prefix_hash = 0
        suffix_hash = 0
        base_power = 1
        longest_palindrome_idx = 0

        for i in range(n):
            prefix_hash = (prefix_hash * BASE + ord(s[i])) % MOD
            suffix_hash = (suffix_hash + ord(s[i]) * base_power) % MOD
            base_power = (base_power * BASE) % MOD
            if prefix_hash == suffix_hash:
                longest_palindrome_idx = i + 1

        suffix_to_add = s[longest_palindrome_idx:]
        return suffix_to_add[::-1] + s
