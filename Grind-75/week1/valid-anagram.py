class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        for c in s:
            if c not in char_map:
                char_map[c] = 1
            else:
                char_map[c] += 1

        for c in t:
            if c not in char_map:
                return False
            else:
                char_map[c] -= 1
                        
        for count in char_map.values():
            if count != 0:
                return False
        
        return True
