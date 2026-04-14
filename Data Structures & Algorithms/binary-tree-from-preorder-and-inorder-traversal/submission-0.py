# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])    # The first element of the the preorder list is always the Root
        mid = inorder.index(root.val)

        # Building the left & right subtrees
        root.left = self.buildTree(preorder[1:(mid+1)], inorder[:mid])
        root.right = self.buildTree(preorder[(mid+1):], inorder[(mid+1):])

        return root