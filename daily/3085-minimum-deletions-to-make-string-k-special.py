from collections import Counter
from itertools import accumulate


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = sorted(Counter(word).values())
        n = len(freq)
        prefix = [0] + list(accumulate(freq))
        ans = float("inf")

        # For each possible base frequency freq[i], aim to bring all character frequencies
        # within the range [freq[i], freq[i] + k]
        # - Delete all characters with frequency < freq[i] (prefix[i])
        # - For characters with frequency > freq[i] + k, delete the excess
        for i in range(n):
            deletion = prefix[i]
            for j in range(i + 1, n):
                if freq[j] > freq[i] + k:
                    deletion += freq[j] - freq[i] - k
            ans = min(ans, deletion)
        return ans
