class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        counts = Counter(tasks)
        for key, value in counts.items():
            maxHeap.append(-1*value)

        heapq.heapify(maxHeap)
        time = 0
        dq = deque()

        while maxHeap or dq:
            time += 1

            if not maxHeap:
                time = dq[0][1]
            else:
                freq_left = heapq.heappop(maxHeap) + 1
                if freq_left:
                    dq.append([freq_left, time + n])     # pair values: [frequecnyLeft, idleTime]

            if dq and dq[0][1] == time:
                heapq.heappush(maxHeap, dq.popleft()[0])

        return time