# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq = collections.deque()
        dq.append(root)
        result = []

        while dq:
            dq_size = len(dq)
            for i in range(0, dq_size):
                node = dq.popleft()

                if not node:
                    continue

                if i == dq_size-1:
                    result.append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return result