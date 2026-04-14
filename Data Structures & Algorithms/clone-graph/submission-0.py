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

        oldToNew = {}       # HashMap: Maps 'Old' to 'New/Cloned'

        def dfs(node):      # Must return the 'Cloned-Node'
            # If the node has already been cloned/visited...
            if node in oldToNew:
                copyNode = oldToNew[node]
            
            # Cloning the node for the first time...
            else:
                copyNode = Node(node.val)       # Create a new Node with a Deep Copy
                oldToNew[node] = copyNode       # Map 'Old-Node' to 'New-Node'

                for nei in node.neighbors:
                    cloned_nei = dfs(nei)
                    copyNode.neighbors.append(cloned_nei)

            return copyNode

        return dfs(node)