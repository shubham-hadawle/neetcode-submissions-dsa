import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Create an Adjacency Matrix, that stores the 'Manhattan Distance' of every edge possible for every node.
        # For the Adjacency Matrix...
        #    key = 'Index of a Node'
        #    value = 'List of [manhattan_dist, node]'
        # NOTE: In the pair-values, we store "distance" first and then the "targer node".
        #       This is done so that the MinHeap can rearrange the nodes to keep the minimum distance at the top to be popped.
        n = len(points)
        adj = collections.defaultdict(list)

        for i in range(0, n):
            xi, yi = points[i]
            for j in range(i+1, n):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append([dist, j])    # [dist, node]
                adj[j].append([dist, i])    # Appending edge for both points/nodes

        # Prim's Algorithm
        cost = 0
        visited = set()
        minHeap = [[0, 0]]      # Initiate the MinHeap with the first node '0' at a distance '0' from itself.
        heapq.heapify(minHeap)
        while len(visited) < n:
            dist, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            cost += dist
            visited.add(i)
            for nei_dist, nei_node in adj[i]:
                if nei_node not in visited:
                    heapq.heappush(minHeap, [nei_dist, nei_node])

        return cost