class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = {"a", "e", "i", "o", "u"}
        prefix_sum = [0] * len(words)
        count = 0
        for i, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                count += 1
            prefix_sum[i] = count

        ans = [0] * len(queries)
        for i, query in enumerate(queries):
            right_count = prefix_sum[query[1]]
            if query[0] == 0:
                left_count = 0
            else:
                left_count = prefix_sum[query[0] - 1]
            ans[i] = right_count - left_count

        return ans
