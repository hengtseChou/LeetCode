class Solution:
    def canConstruct(self, s: str, k: int) -> bool:

        if k > len(s):
            return False

        # instead of iterateing s and save results to a dict
        # using Counter significantly improves runtime

        counts = Counter(s)
        odd_count = 0
        for count in counts.values():
            if count % 2 == 1:
                odd_count += 1
        if odd_count > k:
            return False
        return True
