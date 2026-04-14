class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, soln = [], []
        nums.sort()
        
        def dfs(i):
            if i == len(nums):
                # Valid Subset Found
                result.append(soln.copy())
                return

            # Inclusion Case: All subsets that include nums[i]
            soln.append(nums[i])
            dfs(i + 1)

            # Exclusion Case: All subsets that do NOT include nums[i]
            soln.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:     # Skip all occurrences of nums[i]
                i += 1
            dfs(i + 1)

        dfs(0)
        return list(result)