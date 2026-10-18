class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        hashMapT, window = {}, {}
        for char in t:
            hashMapT[char] = 1 + hashMapT.get(char, 0)

        have, need = 0, len(hashMapT)
        result, resLength = [-1, -1], float("inf")

        for r in range(0, len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in hashMapT and window[s[r]] == hashMapT[s[r]]:
                have += 1

            while have == need:
                if (r-l+1) < resLength:
                    result = [l, r]
                    resLength = r-l+1

                window[s[l]] -= 1
                if s[l] in hashMapT and window[s[l]] < hashMapT[s[l]]:
                    have -= 1
                l += 1
            
        
        if resLength != float("inf"):
            l, r = result
            return s[l: r+1]
        else:
            return ""