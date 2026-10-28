class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        soln = []

        def dfs(i):
            if i >= len(nums):
                result.append(soln.copy())
                return

            soln.append(nums[i])
            i += 1
            
            dfs(i)
            soln.pop()
            dfs(i)

        dfs(0)
        return result