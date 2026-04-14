class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result, soln = [], []
        candidates.sort()
        nums = candidates

        def dfs(i, curr_sum):
            if curr_sum == target:
                # Valid Combination Found
                result.append(soln.copy())
                return

            if curr_sum > target or i >= len(nums):
                # Invalid Combination
                return

            # Inclusion Case: Option 1
            soln.append(nums[i])
            dfs(i+1, curr_sum + nums[i])    # NOTE: Here, we input "i+1" to avoid reusing the element

            # Exclusion Case: Option 2 - Skipping nums[i]
            soln.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, curr_sum)


        dfs(0, 0)       # First call with i=0 & curr_sum=0
        return list(result)