"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {None:None}

        # Iteration 1: create copy-nodes and hashmap
        curr = head
        while curr != None:
            copy_node = Node(curr.val)
            hashmap[curr] = copy_node
            curr = curr.next

        # Iteration 2: create links, 'next' and 'random'
        curr = head
        while curr != None:
            copy_node = hashmap[curr]
            copy_node.next = hashmap[curr.next] # if curr.next != None else None
            copy_node.random = hashmap[curr.random] # if curr.random != None else None
            curr = curr.next

        new_head = hashmap[head]
        return new_head 