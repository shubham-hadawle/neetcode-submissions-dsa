class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p1, p2 = 0, 1
        profit = 0

        while p2 in range(len(prices)):
            if prices[p1] > prices[p2]:
                p1 = p2
                p2 += 1
            else:
                currentProfit = prices[p2] - prices[p1]
                profit = max(currentProfit, profit)
                p2 += 1

        return profit