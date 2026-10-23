import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = {}
        for t in tasks:
            hashMap[t] = 1 + hashMap.get(t, 0)

        maxHeap = []
        heapq.heapify(maxHeap)

        for freq in hashMap.values():
            heapq.heappush(maxHeap, -1 * freq)

        dq = collections.deque()
        time = 0

        while maxHeap or dq:
            time += 1
            if maxHeap:
                freq = heapq.heappop(maxHeap)
                remaining_freq = freq + 1   # Adding +1 as the numbers are negative in the MaxHeap
                if remaining_freq < 0:
                    next_available_time = time + n
                    dq.append([remaining_freq, next_available_time])

            while dq and dq[0][1] == time:
                remaining_freq = dq.popleft()[0]
                heapq.heappush(maxHeap, remaining_freq)

        return time