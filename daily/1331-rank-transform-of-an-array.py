class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique = sorted(set(arr))
        hash_map = {}
        for i, num in enumerate(unique):
            hash_map[num] = i + 1
        rank = [hash_map[num] for num in arr]
        return rank
