class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = { i:[] for i in range(0, n+1) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = [False] * (n+1)
        nodes_in_cycle = set()
        cycleStart = -1

        def dfs(node, prev):
            nonlocal cycleStart
            if visited[node] is True:
                cycleStart = node
                return True

            visited[node] = True

            for neighbour in adj[node]:
                if neighbour == prev:
                    continue
                else:
                    if dfs(neighbour, node) is True:
                        # If cycle is detected, add the node in the 'nodes_in_cycle' set/hashset.
                        if cycleStart != -1:
                            nodes_in_cycle.add(node)

                        # Reset the cycleStart for different cycles.
                        if node == cycleStart:
                            cycleStart = -1
                        
                        return True

            return False

        # Run the DFS once to get all the existing 'nodes in the cycle'.
        flag = dfs(1, -1)

        if flag is True:
            # Iterate edges in reverse order. Return the first edge (u, v) where both endpoints are in cycle.
            for n1, n2 in reversed(edges):
                if n1 in nodes_in_cycle and n2 in nodes_in_cycle:
                    return [n1, n2]
        else:
            return []          