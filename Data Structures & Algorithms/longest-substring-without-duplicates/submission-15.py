class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l, r = 0, 0
        longest = 0
        hashSet = set()

        while r < len(s):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            long = r - l+1
            longest = max(longest, long)
            r += 1

        return longest