class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:

        # It's a Trie problem
        # ref: https://haogroot.com/2021/01/07/trie-leetcode/
        # ref: https://medium.com/@derekfan/%E4%B9%9D%E7%AB%A0%E7%AE%97%E6%B3%95-template-trie-tree-%E5%AD%97%E5%85%B8%E6%A8%B9-132e19c6c827

        prefix_set = set()
        for num in arr1:
            while num > 0:
                prefix_set.add(num)
                num = num // 10

        max_length = 0
        for num in arr2:
            while num > 0:
                if num in prefix_set:
                    max_length = max(max_length, len(str(num)))
                    break  # the longest prefix with current num is found
                else:
                    num = num // 10
        return max_length
