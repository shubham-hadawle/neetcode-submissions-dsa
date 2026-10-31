class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's Algorithm
        hashMap = defaultdict(list)
        indegree = [0] * (numCourses)
        for u, v in prerequisites:
            hashMap[v].append(u)
            indegree[u] += 1

        dq = collections.deque()
        result = []

        for i in range(0, numCourses):
            if indegree[i] == 0:
                dq.append(i)

        while dq:
            for i in range(0, len(dq)):
                node = dq.popleft()
                result.append(node)

                for nei in hashMap[node]:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        dq.append(nei)

        if len(result) < numCourses:
            return []
        return result