class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's Algorithm
        adj = collections.defaultdict(list)
        for u, v in tickets:
            adj[u].append(v)

        # Sorting the values in lexical/alphabetical order
        for i in adj:
            adj[i].sort()
        # OR
        # for v in adj.values():
        #     v.sort()

        itinerary = []
        def dfs(src):
            while adj[src]:
                dest = adj[src].pop(0)
                dfs(dest)
            itinerary.append(src)      # NOTE: It is important to append the src node and then return the reversed path, so as to do the appriopriate DFS and find the correct path.

        dfs("JFK")
        return itinerary[::-1]      # return list(reversed(itinerary))