class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford
        price = [float("inf")] * n
        price[src] = 0

        for i in range(0, k+1):
            tempPrice = price.copy()              # Copy the current Prices into a list of Temporary-Prices

            for s, d, cost in flights:     # s = source node, d = destination node, cost = weight of edge 's to d'
                if price[s] == float("inf"):
                    continue

                if price[s] + cost < tempPrice[d]:
                    tempPrice[d] = price[s] + cost
            
            price = tempPrice

        if price[dst] == float("inf"):
            return -1
        else:
            return price[dst]