class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = collections.defaultdict(list)
        for u, v in tickets:
            adj[u].append(v)

        for v in adj.values():
            v.sort()
        # OR
        # for i  in adj:
        #     adj[i].sort()

        itinerary = []
        def dfs(node):
            while adj[node]:
                next_node = adj[node].pop(0)
                dfs(next_node)
            itinerary.append(node)

        dfs("JFK")
        return list(reversed(itinerary))