class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashMap = {}
        for char in s:
            hashMap[char] = 1 + hashMap.get(char, 0)

        count = 0
        count_with_odd_freq = 0
        for char in hashMap:
            if hashMap[char] % 2 == 0:
                count += hashMap[char]
            else:
                if hashMap[char] > 1:
                    count += hashMap[char] - 1
                count_with_odd_freq += 1

        if count_with_odd_freq > 0:
            count += 1

        return count