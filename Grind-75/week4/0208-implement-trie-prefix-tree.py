# a straight forward hash set method

# class Trie:

#     def __init__(self):
#         self.prefix = set()
#         self.words = set()

#     def insert(self, word: str) -> None:
#         self.words.add(word)
#         for i in range(len(word)):
#             self.prefix.add(word[:(i+1)])

#     def search(self, word: str) -> bool:
#         if word in self.words:
#             return True
#         return False

#     def startsWith(self, prefix: str) -> bool:
#         if prefix in self.prefix:
#             return True
#         return False

# use dict to implement trie node
# more efficient but uses a little bit more memory


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["*"] = True  # Mark the end of the word

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return "*" in node  # Check if it's the end of the word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
