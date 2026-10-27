# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = collections.deque()
        dq.append(root)
        result = []

        while dq:
            answer = []
            for i in range(0, len(dq)):
                node = dq.popleft()

                if not node:
                    continue

                answer.append(node.val)
                dq.append(node.left)
                dq.append(node.right)

            if answer:
                result.append(answer)

        return result