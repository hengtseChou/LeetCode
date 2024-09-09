class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 1. remove non-alphanumeric char and make the remaining into lowercases
        # 2. reverse str
        # 3. check if it is a palindrome

        alnum = ""
        for c in s:
            if c.isalnum():
                alnum = alnum + c.lower()
        if alnum == alnum[::-1]:
            return True
        return False
