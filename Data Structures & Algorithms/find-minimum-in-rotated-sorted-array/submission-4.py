class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minVal = nums[l]

        while l <= r:
            mid = (l + r) // 2

            if nums[l] <= nums[mid]:     # Left Half is SORTED
                minVal = min(minVal, nums[l])
                l = mid + 1
            else:                        # Right Half is SORTED
                minVal = min(minVal, nums[mid])
                r = mid - 1

        return minVal