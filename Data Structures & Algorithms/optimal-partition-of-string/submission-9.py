class Solution:
    def partitionString(self, s: str) -> int:
        if not s:
            return 0

        count = 1
        hashSet = set()
        l, r = 0, 0

        while r < len(s):
            if s[r] in hashSet:
                count += 1
                l = r
                hashSet = set()    # hashSet.clear()
            hashSet.add(s[r])
            r += 1

        return count