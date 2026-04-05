class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        q = deque()

        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)

        finish = 0
        output = []
        while q:
            for _ in range(len(q)):
                crs = q.popleft()
                output.append(crs)
                finish += 1
                
                for nei in adj[crs]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
                

        if finish != numCourses:
            return []
        return output


        
        