class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, node):
        nodeBefore, nodeAfter = node.prev, node.next
        nodeBefore.next = nodeAfter
        nodeAfter.prev = nodeBefore

    def insertAfterHead(self, node):
        nodeAfterHead = self.head.next

        self.head.next = node
        node.prev = self.head
        
        node.next = nodeAfterHead
        nodeAfterHead.prev = node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        # This node is now the most recently used
        self.deleteNode(node)
        self.insertAfterHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            oldNode = self.hashmap[key]
            self.deleteNode(oldNode)
        
        node = ListNode(key, value)
        self.insertAfterHead(node)
        self.hashmap[key] = node

        # If capacity is exceeded remove LRU
        if len(self.hashmap) > self.capacity:
            lruNode = self.tail.prev
            self.deleteNode(lruNode)
            del self.hashmap[lruNode.key]

        
