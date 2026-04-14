class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Cycle Detection using DFS
        # Creating HashMap/Adjacency List to map the courses with relevant prerequisites
        hashmap = { i:[] for i in range(numCourses) }
        for course, pre in prerequisites:
            hashmap[course].append(pre)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if hashmap[course] == []:
                return True

            # If none of the above two conditions are satisfied, then do the following
            visited.add(course)
            for pre in hashmap[course]:
                flag = dfs(pre)
                if not flag:
                    return False
            hashmap[course] = []
            visited.remove(course)
            return True

        for course in range(0, numCourses):
            flag = dfs(course)
            if not flag:
                return False
        return True