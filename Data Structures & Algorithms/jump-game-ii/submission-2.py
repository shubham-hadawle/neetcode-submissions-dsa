class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy Solution
        num_of_jumps = 0
        l, r = 0, 0

        while r < len(nums)-1:      # NOTE: Only Loop till n-1 index
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])

            l = r+1
            r = farthest
            num_of_jumps += 1
        
        return num_of_jumps