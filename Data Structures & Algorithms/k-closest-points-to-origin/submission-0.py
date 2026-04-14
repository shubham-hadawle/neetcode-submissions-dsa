import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        minHeap = []

        for i in range(len(points)):
            x, y = points[i]
            euc_dist = math.sqrt((0-x)**2 + (0-y)**2)
            minHeap.append([euc_dist, x, y])

        heapq.heapify(minHeap)
        # Pop the (x, y) co-ordinates of the first k values into the result
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            result.append([x, y])
            k -= 1

        return result