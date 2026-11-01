class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hashMap = collections.defaultdict(list)
        for u, v, w in times:
            hashMap[u].append((v, w))

        visited = set()

        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, (0, k))

        total_time = 0

        while minHeap:
            dist, node_v = heapq.heappop(minHeap)

            if node_v not in visited:
                visited.add(node_v)
                total_time = max(total_time, dist)

                for nei, w_nei in hashMap[node_v]:
                    if nei in visited:
                        continue
                    heapq.heappush(minHeap, (dist + w_nei, nei))

        if len(visited) == n:
            return total_time
        else:
            return -1