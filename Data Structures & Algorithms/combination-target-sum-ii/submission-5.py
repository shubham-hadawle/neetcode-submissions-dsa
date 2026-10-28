class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        soln = []
        candidates.sort()

        def dfs(i, currSum, soln):
            if currSum == target:
                if soln in result:
                    return
                result.append(soln.copy())
                return

            if currSum > target or i >= len(candidates):
                return

            soln.append(candidates[i])
            dfs(i+1, currSum + candidates[i], soln)

            soln.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, currSum, soln)

            return

        dfs(0, 0, soln)
        return result