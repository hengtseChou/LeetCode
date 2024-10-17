class Solution:
    def maximumSwap(self, num: int) -> int:

        # ref: https://hsiyinl.medium.com/maximum-swap-leetcode-670-f53af43bb719
        # for non-increasing digits, there is no need for swap
        # for sequences that need swap, find the max digit
        # and swap it with the leftmost of the non-increasing part that is smaller than the max digit

        i = 0
        arr = [str(digit) for digit in str(num)]
        while (i < len(arr) - 1) and (int(arr[i]) >= int(arr[i + 1])):
            i += 1
        if i == (len(arr) - 1):
            return num

        j = i + 1
        max_digit, max_idx = -1, j
        while j < len(arr):
            if max_digit <= int(arr[j]):
                max_digit = int(arr[j])
                max_idx = j
            j += 1

        leftmost_idx = 0
        for k in range(i + 1):
            if int(arr[k]) < max_digit:
                leftmost_idx = k
                break

        arr[max_idx], arr[leftmost_idx] = arr[leftmost_idx], arr[max_idx]
        return int("".join(arr))
