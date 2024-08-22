class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        odd = set() # use a set to keep track of the element's value
        length = 0
        for c in s:
            # if c not in odd:
            #     odd.add(c)
            # else:
            #     odd.remove(c)
            #     length += 2
            if c in odd: # faseer in this order
                odd.remove(c)
                length += 2
            else:
                odd.add(c)
        if odd:
            length += 1
        return length
