class Solution:
    def minimumSteps(self, s: str) -> int:

        # we need to move zeroes to the left of ones
        # when encounter zero, calculate how many ones are beforehand
        # that is the steps we need for each zero encountered

        left_zeroes = 0
        steps = 0

        for i, char in enumerate(s):
            if char == "0":
                steps += i - left_zeroes
                left_zeroes += 1
        return steps
