class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i - index)
                maxArea = max(maxArea, area)
                start = index
            stack.append((start, h))

        for i, h in stack:
            area = h * (len(heights) - i)
            maxArea = max(maxArea, area)

        return maxArea