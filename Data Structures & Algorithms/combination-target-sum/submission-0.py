class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, soln = [], []

        def dfs(i, curr_sum):
            if curr_sum == target:
                # Valid Combination Found
                result.append(soln.copy())
                return

            if curr_sum > target or i >= len(nums):
                # Invalid Combination
                return

            # Inclusion Case: Option 1 - Keeping the index unchanged allow reusing the element
            soln.append(nums[i])
            dfs(i, curr_sum + nums[i])

            # Exclusion Case: Option 2
            soln.pop()
            dfs(i + 1, curr_sum)

        dfs(0, 0)   # First call with i=0 & curr_sum=0
        return list(result)
