class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        # Using Sorting
        else:
            s = sorted(s)
            t = sorted(t)
            if s == t:
                return True
            else:
                return False

        # # Using Hashmaps
        # else:
        #     hashS, hashT = {}, {}
        #     for i in range(len(s)):
        #         hashS[s[i]] = 1 + hashS.get(s[i], 0)
        #         hashT[t[i]] = 1 + hashT.get(t[i], 0)

        #     for char in hashS:
        #         if hashS[char] != hashT.get(char, 0):
        #             return False

        #     return True