class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        visit = set()
        def dfs(i):
            if not adj[i]:
                return True
            visit.add(i)
            for nei in adj[i]:
                if nei in visit:
                    return False
                if not dfs(nei):
                    return False
            visit.remove(i)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True