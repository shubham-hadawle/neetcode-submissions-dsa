class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If the graph is empty, then it is definitely a tree.
        if not n:
            return True

        # Create an Adjacency List
        adj = { i:[] for i in range(0, n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)

            for j in adj[i]:
                if j == prev:
                    continue
                flag = dfs(j, i)
                if not flag:
                    return False

            return True

        result = (dfs(0, -1) and n == len(visited))
        return result