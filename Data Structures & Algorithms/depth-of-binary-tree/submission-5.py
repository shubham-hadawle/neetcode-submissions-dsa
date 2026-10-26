# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative BFS using Deque
        if not root:
            return 0

        dq = deque()
        dq.append(root)
        levels = 0
        while dq:
            for i in range(0, len(dq)):
                node = dq.popleft()

                if node.left:
                    dq.append(node.left)

                if node.right:
                    dq.append(node.right)

            levels += 1

        return levels