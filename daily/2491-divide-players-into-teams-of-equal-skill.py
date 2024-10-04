class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        n = len(skill)
        avg = skill[0] + skill[-1]
        ans = 0
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != avg:
                return -1
            ans += skill[i] * skill[n - 1 - i]
        return ans
