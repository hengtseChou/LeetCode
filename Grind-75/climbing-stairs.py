class Solution:
    def climbStairs(self, n: int) -> int:
        from math import factorial

        counts = 0
        max_two_steps = n // 2
        counts += 1 # for all 1 steps
        for i in range(1, max_two_steps + 1):
            one_steps = n - 2 * i
            total_comb = i + one_steps
            counts += int(factorial(total_comb)/(factorial(i) * factorial(one_steps)))
        return counts
