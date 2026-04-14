# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        dq = deque([root])

        while dq:
            rightSide = None
            len_dq = len(dq)
            for i in range(len_dq):
                node = dq.popleft()
                if node:
                    rightSide = node
                    dq.append(node.left)
                    dq.append(node.right)
            
            if rightSide:
                result.append(rightSide.val)

        return result