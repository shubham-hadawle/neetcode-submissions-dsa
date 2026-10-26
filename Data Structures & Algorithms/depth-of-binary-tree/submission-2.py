# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        levels = 0
        maxDepth = 0

        def dfs(node):
            nonlocal levels, maxDepth
            if not node:
                return

            levels += 1
            maxDepth = max(maxDepth, levels)
            dfs(node.left)
            dfs(node.right)
            levels -= 1
            return

        dfs(root)
        return maxDepth