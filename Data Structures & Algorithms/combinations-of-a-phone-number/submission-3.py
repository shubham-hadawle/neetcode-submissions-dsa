class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []
        soln = ""

        hashMap = {
            1: "",
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        def dfs(idx):
            nonlocal result, soln

            if len(soln) == len(digits):
                result.append(soln)
                return

            if idx >= len(digits):
                return

            number = int(digits[idx])
            for char in hashMap[number]:
                soln = soln + char
                dfs(idx+1)
                soln = soln[:-1]

            return

        dfs(0)
        return result