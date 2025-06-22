class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        ans = []
        for i in range(0, n, k):
            ans.append(s[i : i + k])
        ans[-1] += fill * (k - len(ans[-1]))
        return ans
