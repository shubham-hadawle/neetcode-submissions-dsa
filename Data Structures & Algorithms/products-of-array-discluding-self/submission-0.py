class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):  # Iterating the array left to right
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):    # Iterating the array right to left
            output[i] *= postfix
            postfix *= nums[i]

        return output