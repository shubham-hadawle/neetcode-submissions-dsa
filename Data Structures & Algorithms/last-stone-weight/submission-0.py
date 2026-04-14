class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Converting the values to Negative (-ve) in order to use the MinHeap as a MaxHeap
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]

        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            diff = abs(first - second)
            heapq.heappush(stones, -diff)   # Push the Negative (-ve) value of the Difference

        if not stones:      # If the heap is empty, return 0
            return 0
        else:
            return abs(stones[0])   # Return the abosulte value

        