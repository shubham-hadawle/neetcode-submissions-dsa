# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag = True

        def dfs(node):
            nonlocal flag

            if not node:
                return 0

            leftL, rightL = 0, 0
            leftL = dfs(node.left)
            rightL = dfs(node.right)

            if abs(leftL - rightL) > 1:
                flag = False

            return 1 + max(leftL, rightL)

        ans = dfs(root)
        return flag