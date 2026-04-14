class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Using 'nlargest()' function
        kMinHeap = heapq.nlargest(k, nums)
        return kMinHeap[-1]


        # # Using MaxHeap
        # for i in range(len(nums)):
        #     nums[i] = -1 * nums[i]

        # maxHeap = nums
        # heapq.heapify(maxHeap)

        # while k > 1:
        #     heapq.heappop(maxHeap)
        #     k -= 1

        # kthLargest = -1 * (heapq.heappop(maxHeap))
        # return kthLargest