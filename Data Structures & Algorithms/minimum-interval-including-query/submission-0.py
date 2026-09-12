import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x : x[0])
        sorted_queries = sorted(queries)

        minHeap = []
        heapq.heapify(minHeap)
        result = {}
        i = 0       # Index to iterate over intervals

        for q in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                    heapq.heappop(minHeap)

            # Don't pop the top valid item, just look-up the answer
            if minHeap:
                result[q] = minHeap[0][0]
            else:
                result[q] = -1

        final_answer = []
        for q in queries:
            final_answer.append(result[q])
        return final_answer
