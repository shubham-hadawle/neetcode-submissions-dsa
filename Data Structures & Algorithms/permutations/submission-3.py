class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(nums):
            result = []

            if len(nums) == 0:
                return [[]]

            permutations = dfs(nums[1:])

            for perm in permutations:
                for i in range(0, len(perm)+1):
                    soln = perm.copy()
                    soln.insert(i, nums[0])
                    result.append(soln)

            return result

        result = dfs(nums)
        return result