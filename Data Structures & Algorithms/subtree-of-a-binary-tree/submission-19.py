# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False

        def dfs(node, subnode):
            if not node and not subnode:
                return True

            if node and subnode and node.val == subnode.val:
                f1 = dfs(node.left, subnode.left)
                f2 = dfs(node.right, subnode.right)
                return (f1 and f2)

            return False

        if dfs(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
