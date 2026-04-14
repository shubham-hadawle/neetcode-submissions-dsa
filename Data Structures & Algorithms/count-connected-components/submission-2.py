class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # adj = [[] for i in range(0, n)]
        adj = { i:[] for i in range(0, n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        count = 0
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for neighbour in adj[node]:
                dfs(neighbour)
            return

        for i in range(0, n):
            if i not in visited:
                dfs(i)
                # Count only after one DFS is completed.
                count += 1

        return count