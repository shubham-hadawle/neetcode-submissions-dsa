class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #### Dijkstra's Algorithm ####

        adj = collections.defaultdict(list)
        for u, v, weight in times:
            adj[u].append((v, weight))

        minHeap = [(0, k)]      # (distance_from_source_to_destination, destination_node)
        heapq.heapify(minHeap)

        visited = set()
        maxTime = 0

        while minHeap:
            distance_k_to_node, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            maxTime = max(maxTime, distance_k_to_node)

            for v, weight in adj[node]:
                if v not in visited:
                    heapq.heappush(minHeap, (distance_k_to_node + weight, v))     # (distance_from_source_to_node + neighbouring_weight, new_neighbour_node)

        if len(visited) == n:
            return maxTime
        else:
            return -1