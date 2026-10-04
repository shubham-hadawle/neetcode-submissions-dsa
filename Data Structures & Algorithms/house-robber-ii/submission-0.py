class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP - Bottom-Up Approach
        if not nums:
            return None
        if len(nums) <= 3:
            return max(nums)

        dp1, dp2 = [-1] * (len(nums)-1), [-1] * len(nums)
        
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        dp2[1], dp2[2] = nums[1], max(nums[1], nums[2])

        # Loop 1 (1 to n-1)
        for i in range(2, len(nums)-1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])

        # Loop 2 (2 to n)
        for i in range(3, len(nums)):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])

        return max(dp1[-1], dp2[-1])

        # # Recurrence
        # OPT(i) = max{OPT(i-2) + nums[i], OPT(i-1)}