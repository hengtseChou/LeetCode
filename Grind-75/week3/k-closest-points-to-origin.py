class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        import heapq

        heap = []
        for x, y in points:
            heap.append((x**2 + y**2, x, y))
        heapq.heapify(heap)

        # for i, point in enumerate(points):
        #     dist = point[0] ** 2 + point[1] ** 2
        #     heapq.heappush(hq, (dist, i))

        # heapify is O(n), while heappush is O(log n)
        # so it will be more efficient to first append then heapify in-place

        ans = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            ans.append((x, y))
        return ans
