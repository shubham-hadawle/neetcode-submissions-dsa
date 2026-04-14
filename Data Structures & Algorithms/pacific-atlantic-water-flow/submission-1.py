class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()


        # Recursive DFS to append node to the respective Ocean's set
        def dfs(r, c, ocean, prevHeight):
            if ((r < 0) or (r >= ROWS) or (c < 0) or (c >= COLS) or \
                ((r, c) in ocean) or (heights[r][c] < prevHeight)):
                return
            else:
                ocean.add((r, c))
                dfs(r+1, c, ocean, heights[r][c])
                dfs(r-1, c, ocean, heights[r][c])
                dfs(r, c+1, ocean, heights[r][c])
                dfs(r, c-1, ocean, heights[r][c])


        # Call DFS from all the border nodes
        for c in range(0, COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(0, ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])


        # Append the nodes to the Resulting List if the node lets water flow to both the oceans
        result = []
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if (r, c) in pac and (r, c) in atl:
                    result.append([r, c])   # Append as a list
        return result