# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def checkSame(p, q):
            if not p and not q:
                return True

            # If either one is Null/None they are not the same
            if (p and not q) or (not p and q):
                return False

            lCheck = checkSame(p.left, q.left)
            rCheck = checkSame(p.right, q.right)

            if lCheck and rCheck:
                # Check if the values are the same
                if p.val == q.val:
                    return True
            
            return False

        bool_flag = checkSame(p, q)
        return bool_flag