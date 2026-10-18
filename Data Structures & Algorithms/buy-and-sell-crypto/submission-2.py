class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_diff = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                max_diff = max(max_diff, diff)
                r += 1
            else:
                l = r
                r = l+1

        return max_diff