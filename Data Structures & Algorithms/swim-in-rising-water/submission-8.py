class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        minHeap = []
        heapq.heapify(minHeap)
        time = 0
        r, c = 0, 0
        heapq.heappush(minHeap, [time, r, c])

        visited = set()
        maxHeight = grid[0][0]

        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue

            visited.add((r, c))
            maxHeight = max(maxHeight, time)

            if (r, c) == (n-1, n-1):
                return maxHeight

            if r+1 < n:
                heapq.heappush(minHeap, (grid[r+1][c], r+1, c))
            if r-1 >= 0:
                heapq.heappush(minHeap, (grid[r-1][c], r-1, c))
            if c+1 < n:
                heapq.heappush(minHeap, (grid[r][c+1], r, c+1))
            if c-1 >= 0:
                heapq.heappush(minHeap, (grid[r][c-1], r, c-1))

        return maxHeight