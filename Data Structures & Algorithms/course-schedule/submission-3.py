class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        visit = set()
        def dfs(i):
            if i not in adj:
                return True
            
            visit.add(i)
            for nei in adj[i]:
                if nei in visit or not dfs(nei):
                    return False
            visit.remove(i)
            adj[i] = []
            return True
                


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True