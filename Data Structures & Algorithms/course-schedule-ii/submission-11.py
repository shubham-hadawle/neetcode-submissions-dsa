class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashMap = defaultdict(list)
        for u, v in prerequisites:
            hashMap[u].append(v)

        result = []
        visited = set()

        def dfs(i):
            if i in visited:
                return False

            visited.add(i)
            
            for nei in hashMap[i]:
                flag = dfs(nei)
                if not flag:
                    return False

            visited.remove(i)
            hashMap[i] = []
            if hashMap[i] == []:
                # In-Degree has become Zero
                if i not in result:
                    result.append(i)
                    
            return True

        for i in range(0, numCourses):
            flag = dfs(i)
            if not flag:
                return []

        return result