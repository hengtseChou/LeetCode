class Solution:
    def maxScore(self, s: str) -> int:
        
        total_ones = s.count('1')

        left_zeroes = 0
        right_ones = total_ones

        max_score = 0

        for char in s[:-1]:
            if char == "0":
                left_zeroes += 1
            else:
                right_ones -= 1
            max_score = max(max_score, left_zeroes + right_ones)

        return max_score
