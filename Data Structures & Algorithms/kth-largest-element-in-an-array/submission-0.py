class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Using 'nlargest()' function
        kMinHeap = heapq.nlargest(k, nums)
        return kMinHeap[-1]