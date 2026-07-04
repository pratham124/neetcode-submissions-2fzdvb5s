class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list) 
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        

        def bfs(s, d):
            if s not in adj or d not in adj:
                return -1
            q = deque([(s, 1)])
            visit = set()
            while q:
                for _ in range(len(q)):
                    variable, value = q.popleft()
                    if variable == d:
                        return value
                    visit.add(variable)
                    for nei, v in adj[variable]:
                        if nei in visit:
                            continue
                        q.append((nei, value * v))
            return -1

        return [bfs(q[0], q[1]) for q in queries]