class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        currGasBalance = 0
        l, r = 0, 0

        for r in range(0, len(gas)):
            currGasBalance = currGasBalance + gas[r] - cost[r]
            if currGasBalance < 0:
                currGasBalance = 0
                l = r+1

        return l