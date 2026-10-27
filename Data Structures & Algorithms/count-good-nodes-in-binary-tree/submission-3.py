# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        maxVal = 0
        count = 0

        def dfs(node, maxVal):
            nonlocal count

            if not node:
                return

            if node.val >= maxVal:
                count += 1

            dfs(node.left, max(maxVal, node.val))
            dfs(node.right, max(maxVal, node.val))

        dfs(root, root.val)
        return count