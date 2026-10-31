class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        hashMap = defaultdict(list)
        for u, v in edges:
            hashMap[u].append(v)
            hashMap[v].append(u)

        visited = set()
        cycle_nodes = set()
        cycleStart = -1

        def dfs(i, prev):
            nonlocal visited, cycle_nodes, cycleStart

            if i in visited:
                cycleStart = i
                cycle_nodes.add(i)
                return True

            visited.add(i)

            for nei in hashMap[i]:
                if nei == prev:
                    continue

                flag = dfs(nei, i)
                if flag:
                    if cycleStart != -1:
                        cycle_nodes.add(i)

                    if i == cycleStart:
                        cycleStart = -1
                    
                    return True

            return False

        flag = dfs(1, -1)
        if flag:
            for u, v in reversed(edges):
                if u in cycle_nodes and v in cycle_nodes:
                    return [u, v]
            return []