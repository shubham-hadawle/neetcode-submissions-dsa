class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result, soln = [], []
        hashmap = { "2": "abc",
                    "3": "def",
                    "4": "ghi",
                    "5": "jkl",
                    "6": "mno",
                    "7": "pqrs",
                    "8": "tuv",
                    "9": "wxyz"}

        def dfs(i):
            if i == len(digits):
                # Valid Combination Found
                result.append("".join(soln))
                return

            for c in hashmap[digits[i]]:
                soln.append(c)
                dfs(i + 1)
                soln.pop()

        if not digits or digits == "":
            return []   # Return empty list if there are no digits

        dfs(0)
        return result