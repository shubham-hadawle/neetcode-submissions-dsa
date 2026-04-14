class Solution:
    def findMin(self, nums: List[int]) -> int:
        #  l, r = 0, len(num)-1
        #  result = nums[0]

        #  while l <= r:
        #     if nums[l] < nums[r]:
        #         res = min(res, nums[l])
        #         break

        #     mid = (l + r) // 2

        #     if nums[l] <= nums[mid]:

        l, r = 0, len(nums)-1
        minValue = nums[0]

        while l <= r:
            mid = (l + r) // 2

            # if nums[mid] == target:
            #     return target
            # condition to check if Left side is sorted
            if nums[l] <= nums[mid]:
                minValue = min(minValue, nums[l])
                l = mid + 1
            # else the Right side is sorted
            else:
                minValue = min(minValue, nums[mid])
                r = mid - 1

        return minValue
