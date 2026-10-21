class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashMap = {}
        self.left = Node(float("-inf"), float("-inf"))    # Dummy Node for LRU Node
        self.right = Node(float("inf"), float("inf"))   # Dummy Node for MRU Node
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev = node.prev
        next = node.next
        next.prev = prev
        prev.next = next

    def insert_right(self, node):
        new_node = node

        second_last_node = self.right.prev
        new_node.prev = second_last_node
        new_node.next = self.right
        self.right.prev = new_node
        second_last_node.next = new_node

    def get(self, key: int) -> int:
        if key in self.hashMap:
            node = self.hashMap[key]
            self.remove(node)
            self.insert_right(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:            
        if key in self.hashMap:
            node = self.hashMap[key]
            self.remove(node)

        self.hashMap[key] = Node(key, value)
        self.insert_right(self.hashMap[key])
        
        if len(self.hashMap) > self.cap:
            lru_node = self.left.next
            self.remove(lru_node)
            del self.hashMap[lru_node.key]