import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: x[0])
        sorted_queries = sorted(queries)

        minHeap = []
        heapq.heapify(minHeap)
        hashMap = {}

        i = 0
        for q in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            if minHeap and minHeap[0][1] >= q:
                hashMap[q] = minHeap[0][0]
            else:
                hashMap[q] = -1

        result = []
        for q in queries:
            result.append(hashMap[q])

        return result