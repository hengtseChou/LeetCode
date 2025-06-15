class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        # find max
        for c in s:
            if c != "9":
                max_num = int(s.replace(c, "9"))
                break
        else:
            max_num = num

        # find min
        if s[0] != "1":
            min_num = int(s.replace(s[0], "1"))
        else:
            for c in s[1:]:
                if c not in {"0", "1"}:
                    min_num = int(s.replace(c, "0"))
                    break
            else:
                min_num = num

        return max_num - min_num
