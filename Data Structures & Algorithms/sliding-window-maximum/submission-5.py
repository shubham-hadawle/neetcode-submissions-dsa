from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # # Brute Force
        # output = []
        # for l in range(len(nums)-k+1):
        #     maxElem = nums[l]
        #     for r in range(nums.index(maxElem), l+k):
        #         maxElem = max(maxElem, nums[r])
        #     output.append(maxElem)
        # return output

        # Deuqe + Sliding Window
        output = []
        l, r = 0, 0
        dq = deque()

        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            if l  > dq[0]:
                dq.popleft()

            if (r+1) >= k:
                output.append(nums[dq[0]])
                l += 1
            r += 1
        return output