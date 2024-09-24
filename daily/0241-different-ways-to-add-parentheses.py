class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Divide and Conquer
        # ref: https://www.cnblogs.com/grandyang/p/4682458.html
        ans = []
        for i, char in enumerate(expression):
            if char == "+" or char == "-" or char == "*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[(i + 1) :])
                for j, char_left in enumerate(left):
                    for k, char_right in enumerate(right):
                        if char == "+":
                            ans.append(int(char_left) + int(char_right))
                        elif char == "-":
                            ans.append(int(char_left) - int(char_right))
                        else:
                            ans.append(int(char_left) * int(char_right))
        if not ans:
            return [int(expression)]
        return ans
