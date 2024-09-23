class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        # Let dp[i] represent the minimum number of extra characters
        # needed for the substring s[0:i]

        # For each i, you consider two possibilities:
        # If a substring s[j:i] (where 0 ≤ j < i) is in the dictionary,
        # you attempt to use that substring, and the new cost will be dp[j]
        # (the best result for the prefix ending at j)
        # because no extra characters are added for that valid word.
        # Otherwise, you count each character as an "extra" (i.e., add 1 to the previous state).

        n = len(s)
        word_set = set(dictionary)

        # dp[i] represents the minimum number of extra characters left over
        # if we consider the substring s[:i] (i.e., up to but not including i)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1  # Assume the current character is not used
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])  # Use the word s[j:i]

        return dp[n]
