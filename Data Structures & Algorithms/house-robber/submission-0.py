class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP - Bottom-Up Approch
        if not nums:
            return -1
        if len(nums) <= 2:
            return max(nums)

        dp = [-1] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            if nums[i] + dp[i-2] > dp[i-1]:
                dp[i] = nums[i] + dp[i-2]
            else:
                dp[i] = dp[i-1]

        return dp[i]

        # # Recurrence
        # if ith house is included:
        #     OPT{i} = nums[i] + OPT{i-2}
        # else:
        #     OPT{i} = OPT{i-1}