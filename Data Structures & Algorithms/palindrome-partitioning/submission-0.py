class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, soln = [], []

        def dfs(i):
            if i >= len(s):
                result.append(soln.copy())
                return

            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    soln.append(s[i : j+1])     # Append the substring.
                    dfs(j + 1)      # Increase index to cut the partition.
                    soln.pop()      # After the recursive call, pop the current substring.

        def isPalindrome(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True

        dfs(0)
        return list(result)