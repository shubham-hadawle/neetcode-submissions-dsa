# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # result = 0

        def dfs(node, maxVal):
            if not node:
                return 0
            
            if node.val >= maxVal:
                result = 1
            else:
                result = 0
            
            maxVal = max(node.val, maxVal)
            result += dfs(node.left, maxVal)
            result += dfs(node.right, maxVal)
            return result

        result = dfs(root, root.val)
        return result