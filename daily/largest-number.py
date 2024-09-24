class StrNum(str):
    def __lt__(x, y):  # less than method
        return int(x + y) > int(y + x)


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        nums = list(map(str, nums))
        # passing nums into custom StrNum that allows special sort (less than) method
        nums = sorted(nums, key=StrNum)
        if nums[0] == "0":
            return "0"
        return "".join(nums)
