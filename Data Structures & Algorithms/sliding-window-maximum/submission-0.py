class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        for l in range(len(nums)-k+1):
            maxElem = nums[l]
            for r in range(l, l+k):
                maxElem = max(maxElem, nums[r])
            output.append(maxElem)

        return output
