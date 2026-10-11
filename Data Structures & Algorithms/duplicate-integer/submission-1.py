class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}

        for n in nums:
            hashMap[n] = 1 + hashMap.get(n, 0)

        for n in hashMap:
            if hashMap[n] > 1:
                return True

        return False