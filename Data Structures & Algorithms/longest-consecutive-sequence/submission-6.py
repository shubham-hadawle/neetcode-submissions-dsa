class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longestSequence = 0

        for num in nums:
            # Checking if the current num is the start of a sequence
            if num-1 not in hashSet:
                next_num = num + 1
                length = 1
                while next_num in hashSet:
                    length += 1
                    next_num += 1
                longestSequence = max(longestSequence, length)

        return longestSequence