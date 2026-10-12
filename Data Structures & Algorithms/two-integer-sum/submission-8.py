class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            if (target - nums[i]) in hashMap:
                a, b = i, hashMap[(target - nums[i])]
                if a < b:
                    return [a, b]
                else:
                    return [b, a]
            else:
                hashMap[nums[i]] = i

        return None
            