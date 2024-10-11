import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        # ref: https://walkccc.me/LeetCode/problems/1942/

        next_unsat_chair = 0
        # using two heapq (priority queue)
        empty_chairs = []
        occupied = []

        # keep track of the friend's index
        for i in range(len(times)):
            times[i].append(i)

        times.sort(key=lambda x: x[0])

        for arrival, leaving, i in times:
            # release the chairs that will be empty prior to current friend's arrival
            while len(occupied) > 0 and occupied[0][0] <= arrival:
                released_chair = heapq.heappop(occupied)[1]
                heapq.heappush(empty_chairs, released_chair)
            if i == targetFriend:
                return empty_chairs[0] if len(empty_chairs) > 0 else next_unsat_chair
            if len(empty_chairs) == 0:
                heapq.heappush(occupied, (leaving, next_unsat_chair))
                next_unsat_chair += 1
            else:
                empty_chair = heapq.heappop(empty_chairs)
                heapq.heappush(occupied, (leaving, empty_chair))
