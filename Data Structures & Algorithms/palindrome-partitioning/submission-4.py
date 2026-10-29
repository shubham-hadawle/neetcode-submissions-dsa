class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        soln = []

        def dfs(idx):
            if idx == len(s):
                result.append(soln.copy())
                return

            for j in range(idx, len(s)):
                flag = isPalindrome(s, idx, j)
                if flag:
                    soln.append(s[idx:j+1])
                    dfs(j+1)
                    soln.pop()

        def isPalindrome(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        dfs(0)
        return result