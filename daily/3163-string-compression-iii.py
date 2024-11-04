class Solution:
    def compressedString(self, word: str) -> str:

        ans = ""
        curr, count = word[0], 1
        for char in word[1:]:
            if char == curr:
                count += 1
                if count == 10:
                    ans += str(9) + curr
                    count = 1
            else:
                ans += str(count) + curr
                curr = char
                count = 1
        ans += str(count) + curr
        return ans
