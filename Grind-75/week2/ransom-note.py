class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine_current = magazine
        for r in ransomNote:
            if r not in magazine_current:
                return False
            else:
                not_found = True
                for idx, m in enumerate(magazine_current):
                    if r == m:
                        magazine_current = magazine_current[:idx] + magazine_current[(idx + 1):]
                        not_found = False
                        break
                if not_found:
                    return False       
        return True
