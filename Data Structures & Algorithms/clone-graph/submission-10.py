"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        hashMap = {}    # Maps the Original Node to the Copy

        def dfs(node):
            if node in hashMap:
                copy_node = hashMap[node]
                return copy_node

            copy_node = Node(node.val)
            hashMap[node] = copy_node

            # Making the neighbours of the Copy Node
            for nei in node.neighbors:
                copy_nei = dfs(nei)
                copy_node.neighbors.append(copy_nei)

            return copy_node

        root = dfs(node)
        return root