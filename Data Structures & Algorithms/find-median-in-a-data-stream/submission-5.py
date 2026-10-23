import heapq

class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        heapq.heapify(self.small)
        heapq.heapify(self.large)

    def addNum(self, num: int) -> None:
        if self.small and num < (-1 * self.small[0]):
            heapq.heappush(self.small, (-1 * num))
        else:
            heapq.heappush(self.large, num)

        if self.small and self.large:
            if self.small[0] > self.large[0]:
                n = -1 * heapq.heappop(self.small)
                heapq.heappush(self.large, n)

        while abs(len(self.small) - len(self.large)) > 1:
            if len(self.small) > len(self.large):
                n = -1 * heapq.heappop(self.small)
                heapq.heappush(self.large, n)
            else:
                n = -1 * heapq.heappop(self.large)
                heapq.heappush(self.small, n)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            n1, n2 = (-1 * self.small[0]), self.large[0]
            median = (n1 + n2) / 2.0
            return median
        else:
            median = (-1 * self.small[0]) if len(self.small) > len(self.large) else self.large[0]
            return median