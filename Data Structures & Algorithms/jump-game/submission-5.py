class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy Approach - Reverse/Backwards Traversal
        goal = len(nums)-1

        # Loop backwards from last-index to -1 index (NOTE: go further down of index 0)
        for i in range(len(nums)-1, -1, -1):
            if i+nums[i] >= goal:
                goal = i

        if goal == 0:
            return True
        else:
            return False