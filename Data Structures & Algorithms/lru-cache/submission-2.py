class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            value = self.dict[key]
            del self.dict[key]
            self.dict[key] = value  # Bring the key-value pair at the last (most recent) position
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            del self.dict[key]
            self.dict[key] = value
        else:
            if len(self.dict) < self.capacity:
                self.dict[key] = value
            else:       # Length exceed the capacity
                first_key = list(self.dict)[0]
                del self.dict[first_key]
                self.dict[key] = value
        
