# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Check if None or Leaf Node
        if not root:
            return None

        # Swap the Left and Right Nodes
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursive Calls
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root