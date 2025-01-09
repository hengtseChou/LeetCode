class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        ans = 0
        pref_len = len(pref)
        for word in words:
            if word[:pref_len] == pref:
                ans += 1
        return ans
