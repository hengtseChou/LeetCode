class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        # use a set to keep track of what char had occurred
        prefix_a = set()
        prefix_b = set()
        count = 0
        n = len(A)
        ans = [0] * n
        for i in range(n):
            prefix_a.add(A[i])
            prefix_b.add(B[i])
            if A[i] == B[i]:
                count += 1
                ans[i] = count
                continue
            if A[i] in prefix_b:
                count += 1
            if B[i] in prefix_a:
                count += 1
            ans[i] = count
        return ans
