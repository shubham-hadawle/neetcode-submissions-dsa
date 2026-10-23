import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Implementing MaxHeap using -ve conversion of values with a MinHeap
        minHeap = []
        heapq.heapify(minHeap)

        for n in nums:
            heapq.heappush(minHeap, (-1 * n))

        for i in range(0, k-1):
            heapq.heappop(minHeap)

        return (-1 * minHeap[0])