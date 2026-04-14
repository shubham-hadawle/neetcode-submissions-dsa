class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Brute Force
        l, r = 0, len(heights) - 1
        result = 0

        while l < r:
            area = (r-l) * (min(heights[l], heights[r]))
            result = max(result, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            elif heights[l] == heights[r]:
                if heights[l+1] > heights[r-1]:
                    l += 1
                else:
                    r -= 1
            
        return result