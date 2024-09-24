class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if s == " ":
            return 1

        # max_length = 1
        # for i, _ in enumerate(s):
        #     substring = s[i]
        #     for j in range(i + 1, len(s) + 1):
        #         substring = s[i:j]
        #         if len(substring) != len(set(substring)):
        #             break
        #         else:
        #             max_length = max(len(substring), max_length)
        # return max_length

        # use sliding window approach can keep the continuity
        # more about sliding window: https://medium.com/技術筆記/演算法筆記系列-two-pointer-與sliding-window-8742f45f3f55
        left = 0
        max_length = 0
        charset = set()

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            max_length = max(len(charset), max_length)

        return max_length
