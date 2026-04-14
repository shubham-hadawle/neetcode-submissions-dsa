class Solution:
    def trap(self, height: List[int]) -> int:
        # Two Pointers (Left & Right)
        waterStored = 0
        l, r = 0, len(height)-1
        maxLeft, maxRight = height[l], height[r]
        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                waterStored = waterStored + (maxLeft - height[l])
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                waterStored = waterStored + (maxRight - height[r])
        return waterStored