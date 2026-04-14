# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#          self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def serial_dfs(node):
            if not node:
                res.append("N")
                return

            res.append(str(node.val))
            serial_dfs(node.left)
            serial_dfs(node.right)

        serial_dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0      # 'self.' is used so that we may not need to use nonlocal

        def deserial_dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1
            node.left = deserial_dfs()
            node.right = deserial_dfs()
            return node

        result = deserial_dfs()
        return result