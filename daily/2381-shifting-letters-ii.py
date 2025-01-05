class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        
        # keyword: line sweep
        # diff[i] indicates the incremental change to the shift value starting at index i
        #  diff[end + 1] ensures that the effect of the shift stops after the end index
        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            diff[start] += shift_value
            diff[end + 1] -= shift_value
        
        # Compute the net shifts using prefix sums
        net_shifts = [0] * n
        current_shift = 0
        for i in range(n):
            current_shift += diff[i]
            net_shifts[i] = current_shift
        
        # Apply the net shifts to each character
        result = []
        for i in range(n):
            original_index = ord(s[i]) - ord('a')
            new_index = (original_index + net_shifts[i]) % 26
            result.append(chr(ord('a') + new_index))
        
        return ''.join(result)
