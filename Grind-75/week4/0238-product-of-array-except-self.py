class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # method 1

        # n = len(nums)

        # prefix_prod = [1] * n
        # suffix_prod = [1] * n

        # for i in range(1, n):
        #     prefix_prod[i] = prefix_prod[i - 1] * nums[i - 1]
        #     suffix_prod[n - i - 1] = suffix_prod[n - i] * nums[n - i]

        # ans = [prefix_prod[i] * suffix_prod[i] for i in range(n)]
        # return ans

        # method 2

        n = len(nums)
        ans = [1] * n

        left_prod = 1
        for i in range(n):
            ans[i] = left_prod
            left_prod *= nums[i]

        right_prod = 1
        for i in range(n - 1, -1, -1):  # stops at i=0
            ans[i] *= right_prod
            right_prod *= nums[i]

        return ans
