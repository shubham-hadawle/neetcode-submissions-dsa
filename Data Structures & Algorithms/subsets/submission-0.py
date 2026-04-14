class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, soln = [], []

        def dfs(i):
            if i >= len(nums):
                result.append(soln.copy())
                return

            # Inclusion Case for nums[i]
            soln.append(nums[i])
            dfs(i+1)

            # Exclusion Case for nums[i]
            soln.pop()      # Backtracking Step - Pop the recently appended element
            dfs(i+1)

        dfs(0)
        return result