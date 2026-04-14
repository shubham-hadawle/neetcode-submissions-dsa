# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced_flag = [True]

        def calHeight(curr):
            if not curr:
                return 0

            left_height = calHeight(curr.left)
            if balanced_flag[0] == False:
                return -1
            right_height = calHeight(curr.right)

            if abs(left_height - right_height) > 1:
                balanced_flag[0] = False
                return -1

            return 1 + max(left_height, right_height)

        calHeight(root)
        return balanced_flag[0]