class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        concat = " ".join([s1, s2])
        words = concat.split(" ")
        hash_map = {}
        for word in words:
            if word in hash_map:
                hash_map[word] += 1
            else:
                hash_map[word] = 1
        ans = [word for word, count in hash_map.items() if count == 1]
        return ans
