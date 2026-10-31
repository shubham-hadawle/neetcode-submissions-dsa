class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hashMap = defaultdict(list)
        for u, v in edges:
            hashMap[u].append(v)
            hashMap[v].append(u)

        visited = set()
        new_graph_length = 0

        def dfs(i, prev):
            nonlocal new_graph_length

            if i in visited:
                return False

            visited.add(i)
            new_graph_length += 1

            for nei in hashMap[i]:
                if nei == prev:
                    continue
                flag = dfs(nei, i)
                if not flag:
                    return False

            # visited.remove(i)
            return True

        flag = dfs(0, -1)
        if not flag:
            return False

        if new_graph_length == n:
            return True
        else:
            return False