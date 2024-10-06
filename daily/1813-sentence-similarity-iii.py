class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        # use indexes instead of string concat is better

        words1 = sentence1.split()
        words2 = sentence2.split()
        if len(words1) < len(words2):
            words1, words2 = words2, words1

        # Check prefix similarity
        i = 0
        while i < len(words2) and words1[i] == words2[i]:
            i += 1

        # Check suffix similarity
        # Only look for words that are not covered by prefix
        j = 0
        while j < len(words2) - i and words1[len(words1) - 1 - j] == words2[len(words2) - 1 - j]:
            j += 1

        # Check if all words of the shorter sentence are covered either by prefix or suffix
        return i + j >= len(words2)
