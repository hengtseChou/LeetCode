class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        last_char = ""
        count = 0
        for char in s:
            if char != last_char:
                ans.append(char)
                last_char = char
                count = 1
            else:
                if count == 2:
                    continue
                else:
                    ans.append(char)
                    count += 1
        return "".join(ans)
