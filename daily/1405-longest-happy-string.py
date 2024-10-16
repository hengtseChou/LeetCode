import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        # ref: https://algo.monster/liteproblems/1405

        max_heap = []
        ans = []
        if a > 0:
            heapq.heappush(max_heap, [-a, 'a'])
        if b > 0:
            heapq.heappush(max_heap, [-b, 'b'])
        if c > 0:
            heapq.heappush(max_heap, [-c, 'c'])

        while max_heap:
            curr_char = heapq.heappop(max_heap)
            if len(ans) >= 2 and ans[-1] == curr_char[1] and ans[-2] == curr_char[1]:
                if not max_heap:
                    break
                next_char = heapq.heappop(max_heap)
                ans.append(next_char[1])
                if -next_char[0] > 1:
                    next_char[0] += 1
                    heapq.heappush(max_heap, next_char)
                heapq.heappush(max_heap, curr_char)

            else:
                ans.append(curr_char[1])
                if -curr_char[0] > 1:
                    curr_char[0] += 1
                    heapq.heappush(max_heap, curr_char)
        
        return "".join(ans)

        
