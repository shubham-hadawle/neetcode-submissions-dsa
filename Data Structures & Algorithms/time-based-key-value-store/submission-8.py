class TimeMap:

    def __init__(self):
        self.hashmap = {}   # key : value (list of [values, timestamp])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key] = self.hashmap.get(key, [])
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Use Binary Search
        valueItems = self.hashmap.get(key, [])
        l, r = 0, len(valueItems)-1
        output = ""

        while l <= r:
            mid = (l + r) // 2
            if valueItems[mid][1] <= timestamp:
                if key in self.hashmap:
                    output = valueItems[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return output