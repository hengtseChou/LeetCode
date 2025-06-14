class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)

        # For max: replace the first non-9 digit with '9'
        for c in num_str:
            if c != "9":
                max_num = int(num_str.replace(c, "9"))
                break
        # this else block only executes if the loop did not break
        else:
            max_num = num

        # For min: replace the first digit with '0'
        min_num = int(num_str.replace(num_str[0], "0"))

        return max_num - min_num
