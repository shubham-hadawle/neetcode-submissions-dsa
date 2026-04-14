class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        hashmap = { i:[] for i in range(numCourses) }
        for course, pre in prerequisites:
            hashmap[course].append(pre)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if hashmap[course] == []:
                if course not in result:
                    result.append(course)
                return True

            visited.add(course)
            for pre in hashmap[course]:
                flag = dfs(pre)
                if not flag:
                    return False
            visited.remove(course)
            hashmap[course] = []
            if course not in result:
                result.append(course)
            return True

        for course in range(0, numCourses):
            flag = dfs(course)
            if not flag:
                return []

        return result