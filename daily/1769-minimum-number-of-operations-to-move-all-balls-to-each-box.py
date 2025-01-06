class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        n = len(boxes)
        ans = [0] * n

        # prefix: operations needed so far
        # count: balls encountered so far
        prefix, count = 0, 0
        for i in range (n):
            prefix += count
            ans[i] += prefix
            if boxes[i] == "1":
                count += 1
        
        # suffix: operations needed so far
        # count: balls encountered so far
        suffix, count = 0, 0
        for i in range(n - 1, -1, -1):
            suffix += count
            ans[i] += suffix
            if boxes[i] == "1":
                count += 1
        
        return ans

        
