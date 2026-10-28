class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        soln = []

        def dfs(i, currSum, soln):
            if currSum == target:
                result.append(soln.copy())
                return

            if currSum > target or i >= len(nums):
                return

            # Recursive call Including the Current Number while allowing the chances of Repeatedly taking up the Number
            soln.append(nums[i])
            dfs(i, currSum + nums[i], soln)

            # Recursive call that does not Include the Number at all in the Solution
            soln.pop()
            dfs(i+1, currSum, soln)

            return

        dfs(0, 0, soln)
        return result