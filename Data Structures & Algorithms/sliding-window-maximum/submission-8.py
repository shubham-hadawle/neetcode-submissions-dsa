class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        result = []
        dq = collections.deque()    # monotonically decreasing queue that stores the number's index

        while r < len(nums):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()    # remove elements from right if they are smaller than nums[r]
            dq.append(r)

            # remove leftmost element if sliding window has moved ahead
            if l > dq[0]:
                dq.popleft()

            # handling starting elements till window is at least size k
            if (r+1) >= k:
                result.append(nums[dq[0]])
                l += 1

            r += 1

        return result