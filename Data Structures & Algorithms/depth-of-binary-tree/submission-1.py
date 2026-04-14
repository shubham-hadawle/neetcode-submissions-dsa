# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive Depth First Search
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # # Iterative BFS (Deque)
        # if not root:
        #     return 0

        # depth = 0
        # dq = deque([root])
        # while dq != None:
        #     for i in range(0, len(dq)):
        #         node = dq.popleft()

        #         if node.left != None:
        #             dq.append(node.left)
        #         if node.right != None:
        #             dq.append(node.right)
        #     depth += 1
        # return depth

        # # Iterative DFS with Stack
        # stack = [[root, 1]]
        # result = 0
        # while stack:
        #     node, depth = stack.pop()

        #     if node != None:
        #         result = max(result, depth)
        #         if node.left:
        #             stack.append([node.left, depth+1])
        #         if node.right:
        #             stack.append([node.right, depth+1])
        # return result