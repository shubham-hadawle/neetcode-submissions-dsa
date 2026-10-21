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
        hashMap = {}    # key: original_node, value: copy_node
        
        curr = head
        while curr != None:
            copy = Node(curr.val)
            hashMap[curr] = copy
            curr = curr.next

        curr = head
        while curr != None:
            copy = hashMap[curr]
            copy.next = hashMap.get(curr.next, None)
            copy.random = hashMap.get(curr.random, None)
            curr = curr.next

        if head == None:
            return None
        else:
            return hashMap[head]