class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l, r = 0, 0
        hashMap = {}    # key: char, value: last occurrence of char
        for i in range(0, len(s)):
            hashMap[s[i]] = i

        result = []
        end = 0
        strings = []

        while r <= len(s)-1:
            end = max(end, hashMap[s[r]])
            if r == end:
                result.append(r - l + 1)
                strings.append(s[l:r+1])
                l = r+1
            r += 1

        return result