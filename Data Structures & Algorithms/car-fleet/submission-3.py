class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed))
        zipped.sort(key = lambda x: x[0])
        zipped.reverse()
        cars = zipped

        pos, spd = cars[0]
        previous_time = (target - pos)/spd
        car_fleets = 1

        for i in range(1, len(position)):
            pos, spd = cars[i]
            current_time = (target - pos)/spd

            if current_time > previous_time:
                car_fleets += 1
                previous_time = current_time

        return car_fleets