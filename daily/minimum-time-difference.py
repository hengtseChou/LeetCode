class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        minutes = [0] * (len(timePoints))
        for i, time in enumerate(timePoints):
            hours = int(time[:2])
            mins = int(time[3:5])
            minutes[i] = hours * 60 + mins

        minutes.sort()
        minutes.append(minutes[0] + 1440)
        min_diff = 1440

        for i in range(len(minutes) - 1):
            min_diff = min(min_diff, minutes[i + 1] - minutes[i])
        return min_diff
