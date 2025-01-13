class Solution:
    def minimumLength(self, s: str) -> int:
        
        hash_table = Counter(s)
        ans = 0
        for count in hash_table.values():
            if count % 2 == 0:
                ans += 2
            else:
                ans += 1
        return ans
