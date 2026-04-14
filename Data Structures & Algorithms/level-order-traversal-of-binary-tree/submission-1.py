# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        result = []

        dq = deque()
        dq.append(root)
        while dq:
            level = []

            len_dq = len(dq)
            # This for loop will ensure that only the nodes are the current depth are popped
            for i in range(len_dq):
                node = dq.popleft()
                if node:
                    level.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
                
            if level:   # Checks if the list is not empty
                result.append(level)
            
        return result