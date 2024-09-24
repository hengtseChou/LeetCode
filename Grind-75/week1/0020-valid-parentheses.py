class Solution:
    def isValid(self, s: str) -> bool:

        # use a stack(list) implementation
        parentheses = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for char in s:
            if char in parentheses: 
                # the checking with and is done sequentially
                # if not passing then straight go to else           
                if stack and parentheses[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        return False
