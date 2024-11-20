class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        a_total = s.count("a")
        b_total = s.count("b")
        c_total = s.count("c")

        if a_total < k or b_total < k or c_total < k:
            return -1

        l, r = 0, 0
        a, b, c = 0, 0, 0
        n = len(s)
        ans = n

        while r < n:
            if s[r] == "a":
                a += 1
            if s[r] == "b":
                b += 1
            if s[r] == "c":
                c += 1
            r += 1

            # shrink window from left if exceeded limit
            while a > a_total - k or b > b_total - k or c > c_total - k:
                if s[l] == "a":
                    a -= 1
                if s[l] == "b":
                    b -= 1
                if s[l] == "c":
                    c -= 1
                l += 1

            # update by the minimum number of char to remove
            ans = min(ans, n - (r - l))

        return ans
