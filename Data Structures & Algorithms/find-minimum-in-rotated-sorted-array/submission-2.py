class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary Search
        l, r = 0, len(nums)-1
        result = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            
            mid = (l + r) // 2
            result = min(result, nums[mid])
            # Condition to check if we should search in the left sorted array or the right sorted.
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return result

            