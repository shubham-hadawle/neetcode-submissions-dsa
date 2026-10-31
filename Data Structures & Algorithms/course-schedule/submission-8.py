class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjacency List
        hashMap = defaultdict(list)
        for u, v in prerequisites:
            hashMap[u].append(v)

        visited = set()

        def dfs(i):
            if i in visited:
                return False

            visited.add(i)
            for j in hashMap[i]:
                flag = dfs(j)
                if not flag:
                    return False

            visited.remove(i)
            hashMap[i] = []

            return True

        for i in range(0, numCourses):
            flag = dfs(i)
            if not flag:
                return False

        return True