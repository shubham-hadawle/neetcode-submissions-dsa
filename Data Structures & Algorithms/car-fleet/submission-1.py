class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zippedList = list(zip(position, speed))
        sortedList = sorted(zippedList)
        pairs = sortedList[::-1]
        p, s = pairs[0]

        prev_fleet_time_req = (target - p) / s
        fleet = 1

        for i in range(1, len(position)):
            p, s = pairs[i]
            current_car_time_req = (target - p) / s
            if current_car_time_req > prev_fleet_time_req:
                fleet += 1
                prev_fleet_time_req = current_car_time_req
            
        return fleet