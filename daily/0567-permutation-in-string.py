class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # for substring questions, use sliding window
        # find permutation substring = ckeck char count of sliding window

        if len(s1) > len(s2):
            return False

        s1_arr = [0] * 26
        s2_arr = [0] * 26

        a_idx = ord("a")

        for i in range(len(s1)):
            s1_arr[ord(s1[i]) - a_idx] += 1
            s2_arr[ord(s2[i]) - a_idx] += 1

        for i in range(len(s2) - len(s1)):
            if s1_arr == s2_arr:
                return True
            s2_arr[ord(s2[i]) - a_idx] -= 1
            s2_arr[ord(s2[i + len(s1)]) - a_idx] += 1

        return s1_arr == s2_arr
