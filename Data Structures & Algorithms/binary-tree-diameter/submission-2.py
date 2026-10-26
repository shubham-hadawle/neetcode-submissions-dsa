# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0

        diameter = 0

        def dfs(node, length):
            nonlocal diameter

            if not node:
                return 0

            lengthL, lengthR = 0, 0
            if node.left:
                lengthL += dfs(node.left, length+1)

            if node.right:
                lengthR += dfs(node.right, length+1)            

            sum = lengthL + lengthR
            diameter = max(diameter, sum)
            return max(lengthL, lengthR)+1

        dfs(root, 1)
        return diameter