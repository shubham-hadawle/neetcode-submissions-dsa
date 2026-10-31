class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashMap = defaultdict(list)
        for u, v in edges:
            hashMap[u].append(v)
            hashMap[v].append(u)

        visited = set()
        components = 0

        def dfs(i):
            if i in visited:
                return

            visited.add(i)

            for nei in hashMap[i]:
                dfs(nei)

            return

        for i in range(0, n):
            if i not in visited:
                dfs(i)
                components += 1
            else:
                continue

        return components