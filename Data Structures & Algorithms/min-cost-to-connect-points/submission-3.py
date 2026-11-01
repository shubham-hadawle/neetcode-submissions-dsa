class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        hashMap = collections.defaultdict(list)

        n = len(points)
        for i in range(0, n):
            for j in range(i+1, n):
                xi, yi = points[i]
                xj, yj = points[j]

                dist = abs(xi - xj) + abs(yi - yj)

                hashMap[i].append([dist, j])
                hashMap[j].append([dist, i])

        cost = 0
        first_node = 0
        minHeap = []
        heapq.heapify(minHeap)
        heapq.heappush(minHeap, [0, first_node])
        visited = set()

        while len(visited) != n:
            dist, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            cost += dist

            for nei_dist, nei in hashMap[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, [nei_dist, nei])

        return cost