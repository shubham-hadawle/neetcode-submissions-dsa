class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        maxSum = float("-inf")
        currSum = 0

        for i in range(0, len(nums)):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)

            if currSum < 0:
                currSum = 0

        return maxSum