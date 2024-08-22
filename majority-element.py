class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # majority_threshold = len(nums) // 2
        # hash_map = {}
        # for num in nums:
        #     if num not in hash_map:
        #         hash_map[num] = 1
        #     else:
        #         hash_map[num] += 1
        # for key, value in hash_map.items():
        #     if value > majority_threshold:
        #         return key
        # return 0
        # time O(N), space O(N)

        # Boyer–Moore majority vote algorithm
        # time O(N), space O(1)
        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
