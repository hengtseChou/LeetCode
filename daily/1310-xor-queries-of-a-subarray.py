class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        # save the cumulative result beforehand
        # XOR(L, R) = XOR(0, R) ^ XOR(0, L - 1)
        # duplicated terms will be canceled out
        prefix = [0] * (len(arr) + 1)
        prefix[0] = arr[0]
        for i, x in enumerate(arr):
            prefix[i + 1] = prefix[i] ^ x

        ans = [prefix[L] ^ prefix[R + 1] for L, R in queries]
        return ans
