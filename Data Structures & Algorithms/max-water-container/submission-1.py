class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        answer, area = 0, 0

        while l < r:
            area = (r-l) * (min(heights[l], heights[r]))
            answer = max(area, answer)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            elif heights[l] == heights[r]:
                if heights[l+1] > heights[r-1]:
                    l += 1
                elif heights[l+1] < heights[r-1]:
                    r -= 1
                else:       # heights[l] == heights[r]
                    l += 1

        return answer