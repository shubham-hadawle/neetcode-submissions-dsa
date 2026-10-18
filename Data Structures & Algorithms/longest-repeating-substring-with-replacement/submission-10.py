class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        hashMap = {}
        result = 0
        max_freq = 0

        for r in range(0, len(s)):
            hashMap[s[r]] = 1 + hashMap.get(s[r], 0)
            max_freq = max(hashMap.values())

            while (r - l + 1) - max_freq > k:
                hashMap[s[l]] = hashMap[s[l]] - 1
                l += 1

            result = max(result, (r - l + 1))

        return result