# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def calMaxHeight(curr):
            if not curr:
                return 0
            
            lHeight = calMaxHeight(curr.left)
            rHeight = calMaxHeight(curr.right)

            nonlocal diameter
            diameter = max(diameter, (lHeight + rHeight))
            maxHeight = 1 + max(lHeight, rHeight)
            return maxHeight

        calMaxHeight(root)
        return diameter