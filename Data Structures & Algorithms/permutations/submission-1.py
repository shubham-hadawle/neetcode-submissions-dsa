class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, soln = [], []
        n = len(nums)

        def dfs():
            if len(soln) == n:
                # Valid Permutation Found
                result.append(soln.copy())    # Append when, len(soln) = len(nums)

            # DFS with a new number being added
            for x in nums:
                if x not in soln:
                    soln.append(x)
                    dfs()
                    soln.pop()
                    dfs
        
        dfs()
        return list(result)