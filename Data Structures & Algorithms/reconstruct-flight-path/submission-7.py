class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        hashMap = collections.defaultdict(list)
        for u, v in tickets:
            hashMap[u].append(v)

        for val in hashMap.values():
            val.sort()

        result = []

        def dfs(i):
            while hashMap[i]:
                dest = hashMap[i].pop(0)
                dfs(dest)
            result.append(i)

        dfs("JFK")
        return result[::-1]