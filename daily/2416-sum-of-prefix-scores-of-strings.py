class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        from collections import defaultdict

        # prefix_count = defaultdict(int)
        # for word in words:
        #     for i in range(len(word)):
        #         prefix_count[word[:(i + 1)]] += 1
        # scores = [0] * len(words)
        # for i, word in enumerate(words):
        #     score = 0
        #     for j in range(len(word)):
        #         score += prefix_count[word[:(j+1)]]
        #     scores[i] = score
        # return scores

        # String slicing in Python is a relatively expensive operation
        # since each slice creates a new string
        # the trie method avoids repetitive string slicing and redundent dict lookups
        # traversing node is constant time while dict lookup will increase complexity when prefix increases

        class TrieNode:
            def __init__(self):
                self.children = defaultdict(TrieNode)
                self.count = 0

        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                node = node.children[char]
                node.count += 1

        def calc_score(word, root):
            node = root
            score = 0
            for char in word:
                node = node.children[char]
                score += node.count
            return score

        return [calc_score(word, root) for word in words]
