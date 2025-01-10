class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        max_freq = {}
        for word in words2:
            char_freq = {}
            for char in word:
                if char not in char_freq:
                    char_freq[char] = 1
                else:
                    char_freq[char] += 1
            for char, count in char_freq.items():
                if char not in max_freq:
                    max_freq[char] = count
                elif max_freq[char] < count:
                    max_freq[char] = count

        ans = []
        for word in words1:
            char_freq = {}
            for char in word:
                if char not in char_freq:
                    char_freq[char] = 1
                else:
                    char_freq[char] += 1
            is_universal = True
            for char, count in max_freq.items():
                if char not in char_freq or char_freq[char] < count:
                    is_universal = False
                    break
            if is_universal:
                ans.append(word)
        
        return ans
