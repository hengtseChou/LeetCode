class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # using the stack concept to solve this question
        # note:
        # for a list, append() and pop() are O(1)
        # pop(1) or insert(0, x) are O(n) because shifting is required
        # for a deque, append(), pop(), appendleft() and popleft() are all O(1)
        operators = ("+", "-", "*", "/")
        nums = []
        for token in tokens:
            if token not in operators:
                nums.append(int(token))
            else:
                # the insertion order was b -> a
                # default position of pop is -1
                a = nums.pop()
                b = nums.pop()
                if token == "+":
                    nums.append(b + a)
                elif token == "-":
                    nums.append(b - a)
                elif token == "*":
                    nums.append(b * a)
                elif token == "/":
                    # The division between two integers always truncates toward zero
                    if b * a < 0:
                        nums.append((b // (-1 * a)) * -1)
                    else:
                        nums.append(b // a)
        return nums[0]
