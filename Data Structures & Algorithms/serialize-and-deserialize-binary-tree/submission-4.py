# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return
            
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return

        dfs(root)
        result = ','.join(result)
        return result
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        result = data.split(',')
        i = 0

        def dfs(node_val):
            nonlocal i

            if node_val == "N":
                i += 1
                return None

            node_val = int(node_val)
            node = TreeNode(node_val)

            i += 1
            node.left = dfs(result[i])
            node.right = dfs(result[i])

            return node

        root = dfs(result[0])
        return root