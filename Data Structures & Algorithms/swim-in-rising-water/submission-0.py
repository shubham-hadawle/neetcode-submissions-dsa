class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        minHeap = []
        heapq.heapify(minHeap)
        # Adding the starting point to the MinHeap
        heapq.heappush(minHeap, (grid[0][0], 0, 0))     # (time/max_height, r, c)

        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            visited.add((r, c))

            if r == n-1 and c == n-1:
                return t

            for dr, dc in directions:       # This will check all 4 directional neighbours.
                nr, nc = r+dr, c+dc

                if (nr < 0 or nr >= n or 
                    nc < 0 or nc >= n or 
                    (nr, nc) in visited):
                    continue
                
                visited.add((nr, nc))
                newTime = max(t, grid[nr][nc])
                heapq.heappush(minHeap, (newTime, nr, nc))
