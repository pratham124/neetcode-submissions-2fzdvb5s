class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()

        t = 0


        while maxHeap or q:
            t += 1

            if q and q[0][0] == t:
                ready_time, freq = q.popleft()
                heapq.heappush(maxHeap, -freq)

            if maxHeap:
                c = -heapq.heappop(maxHeap)
                c -= 1
                if c:
                    q.append((t + n + 1, c))

        return t
        