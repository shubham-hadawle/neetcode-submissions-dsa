# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        count = 0
        stack = []
        node = root          
        stack.append(node)

        while node or stack:
            while node != None:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            count += 1

            if count == k:
                return node.val
            # Go Right Once
            node = node.right