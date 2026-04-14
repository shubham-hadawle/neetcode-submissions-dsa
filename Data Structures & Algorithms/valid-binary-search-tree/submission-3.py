# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, left_bound, right_bound) -> bool:
            if not node:
                return True
            
            if not (left_bound < node.val and node.val < right_bound):
                return False

            lCheck = dfs(node.left, left_bound, node.val)
            rCheck = dfs(node.right, node.val, right_bound)
            if lCheck and rCheck:
                return True
            else:
                return False

        result = dfs(root, float("-inf"), float("inf"))
        return result