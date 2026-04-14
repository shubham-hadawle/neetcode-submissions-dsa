class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashs1 = [0] * 26      # Hash array of 26 letters
        hashs2 = [0] * 26

        length_of_s1 = len(s1)
        length_of_s2 = len(s2)

        if length_of_s1 > length_of_s2:
            return False

        for i in range(length_of_s1):
            hashs1[ ord(s1[i]) - ord('a') ] += 1
            hashs2[ ord(s2[i]) - ord('a') ] += 1

        if hashs1 == hashs2:
            return True
        
        for i in range(length_of_s1, length_of_s2):
            hashs2[ ord(s2[i]) - ord('a') ] += 1
            hashs2[ ord(s2[i - length_of_s1]) - ord('a') ] -= 1

            if hashs1 == hashs2:
                return True

        return False
