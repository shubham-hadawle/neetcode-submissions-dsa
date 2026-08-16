class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        current_gas_balance = 0
        start_position = 0

        for i in range(0, len(gas)):
            current_gas_balance += (gas[i] - cost[i])

            if current_gas_balance < 0:
                current_gas_balance = 0
                start_position = i + 1

        return start_position