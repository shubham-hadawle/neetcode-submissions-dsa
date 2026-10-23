import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)

        for p in points:
            x, y = p
            dist = math.sqrt((x-0)**2 + (y-0)**2)
            heapq.heappush(minHeap, (dist, [x, y]))

        result = []
        for i in range(0, k):
            dist, coord = heapq.heappop(minHeap)
            result.append(coord)
        
        return result