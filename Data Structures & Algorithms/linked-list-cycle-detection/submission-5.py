# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # # Floyd's Tortoise and Hare
        # # Slow & Fast Pointers
        # slow, fast = head, head

        # while fast != None and fast.next != None:
        #     slow = slow.next        # Slow Pointer travels at 1x speed
        #     fast = fast.next.next   # Fast Pointer travels at 2x speed

        #     if slow == fast:
        #         return True
        
        # # If the condition is not met in the while, there is no cycle
        # return False


        # Hashset - Time & Space Comp: O(n)
        hashset = set()     # Create a set of 'Node' objects
        curr = head

        while curr != None:
            if curr in hashset:
                return True
            else:
                hashset.add(curr)
                curr = curr.next

        return False