class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(0, k+1):
            tempPrices = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue

                if tempPrices[d] > prices[s] + p:
                    tempPrices[d] = prices[s] + p

            prices = tempPrices

        if prices[dst] == float("inf"):
            return -1
        return prices[dst]