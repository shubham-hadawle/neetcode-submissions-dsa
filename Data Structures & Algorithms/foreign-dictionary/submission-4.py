class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = { c: set() for w in words for c in w }

        for i in range(0, len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLength = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLength] == w2[:minLength]:
                return ""
            
            for j in range(0, minLength):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # Creating a Hashmap to detect cycles, by tracking 3-states.
        # If the 'char' maps to False - node if fully processed/visited.
        # If the 'char' maps to True - node is in the current path.
        # If 'char' is not added to the Hashmap - node is unvisited.
        visited = {}
        result = []

        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True       # Currently visiting the node and its path.
            for neighbour in adj[c]:
                if dfs(neighbour) is True:
                    return True
            visited[c] = False      # Node is completely processed without cycles.
            result.append(c)

        for c in adj:
            if dfs(c) is True:
                return ""

        result.reverse()
        return "".join(result)