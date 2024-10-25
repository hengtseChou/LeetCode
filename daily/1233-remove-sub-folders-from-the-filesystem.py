# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, folder):
#         current = self.root
#         parts = folder.split("/")[1:]
#         for part in parts:
#             if current.is_end:
#                 return
#             if part not in current.children:
#                 current.children[part] = TrieNode()
#             current = current.children[part]
#         current.is_end = True

#     def collect_folders(self, node=None, path=""):
#         if node is None:
#             node = self.root
#         result = []
#         if node.is_end:
#             result.append(path)
#             return result
#         for folder, child_node in node.children.items():
#             result.extend(self.collect_folders(child_node, path + "/" + folder))
#         return result

# class Solution:
#     def removeSubfolders(self, folder: List[str]) -> List[str]:


#         trie = Trie()
#         folder.sort()  # Sort folders to ensure parent comes before subfolder
#         for f in folder:
#             trie.insert(f)
#         return trie.collect_folders()
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        folder.sort()
        result = []
        for f in folder:
            # the current folder is not a sub-folder of the last added folder
            if not result or not f.startswith(result[-1] + "/"):
                result.append(f)
        return result
