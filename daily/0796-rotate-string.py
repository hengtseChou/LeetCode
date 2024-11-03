class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False
        # if it can become goal with some shifts
        # then goal should be a substring of s+s
        if goal in s + s:
            return True
        return False
