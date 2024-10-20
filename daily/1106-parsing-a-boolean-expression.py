class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = deque()
        for c in expression:
            if c == "," or c == "(":
                continue
            if c in ["t", "f", "!", "&", "|"]:
                stack.append(c)
            elif c == ")":
                has_true = False
                has_false = False
                while stack[-1] not in ["!", "&", "|"]:
                    top_value = stack.pop()
                    if top_value == "t":
                        has_true = True
                    elif top_value == "f":
                        has_false = True
                op = stack.pop()
                if op == "!":
                    stack.append("t" if not has_true else "f")
                elif op == "&":
                    stack.append("f" if has_false else "t")
                else:
                    stack.append("t" if has_true else "f")
        return stack[-1] == "t"
