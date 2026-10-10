class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        res = []
        visit = set()
        seen = set()
        def dfs(i):
            if i in visit:
                return False
            if i in seen:
                return True

            visit.add(i)
            for nei in adj[i]:
                if not dfs(nei):
                    return False
            visit.remove(i)
            seen.add(i)
            res.append(i)
            return True



        for i in range(numCourses):
            if not dfs(i):
                return []
        return res