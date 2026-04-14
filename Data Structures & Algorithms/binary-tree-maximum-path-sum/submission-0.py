# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = root.val      # Base value of result should at least the value of the Root

        def dfs(root):
            if not root:
                return 0
            
            # Calculating maximum-path-sums for left and right subtrees
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(0, leftMax)       # In case, leftMax is -ve
            rightMax = max(0, rightMax)     # In case, rightMax is -ve

            # Update result with the maximum-path-sum
            nonlocal result
            result = max(result, root.val + leftMax + rightMax)

            # Return the maximum-path-sum rooted at this node
            mps_after_split = root.val + max(leftMax, rightMax)
            return mps_after_split

        dfs(root)
        return result