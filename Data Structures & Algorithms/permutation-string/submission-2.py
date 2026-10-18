class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hashMap = {}
        for char in s1:
            hashMap[char] = 1 + hashMap.get(char, 0)

        # Initial Window
        tempHash = {}
        for i in range(0, len(s1)):
            tempHash[s2[i]] = 1 + tempHash.get(s2[i], 0)

        if tempHash == hashMap:
            return True

        # Sliding across the the Remaining Window
        for i in range(len(s1), len(s2)):
            new_char = s2[i]
            tempHash[new_char] = 1 + tempHash.get(new_char, 0)

            left_char = i - len(s1)
            if tempHash[s2[left_char]] > 1:
                tempHash[s2[left_char]] -= 1
            else:
                del tempHash[s2[left_char]]

            if tempHash == hashMap:
                return True
        
        return False