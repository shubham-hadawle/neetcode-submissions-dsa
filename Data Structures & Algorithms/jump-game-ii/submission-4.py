class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        farthest = 0
        no_of_jumps = 0

        while r <= len(nums)-2:     # NOTE: Index r cannot traverse further than 'n-1' as it would account for +1 jumps even from position 'n'.
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])

            no_of_jumps += 1
            l = r+1
            r = farthest

        return no_of_jumps