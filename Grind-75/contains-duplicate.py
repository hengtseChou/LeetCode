class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # or just an one-liner
        # return (len(nums) != len(set(nums)))
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            else:
                hash_set.add(num)
        return False
