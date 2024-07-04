class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # a hashmap (dict) solution
	# hashmap has a O(1) complexity in search
        hashmap = {}
        for i, num in enumerate(nums):
            remain = target - num
            if remain in hashmap.keys():
                return [i, hashmap.get(remain)]
            else:
                hashmap[num] = i
