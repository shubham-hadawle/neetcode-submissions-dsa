# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Flyod's Tortoise and Hare
        # Fast & Slow Pointers
        slow, fast = head, head     # Both start at the same position

        while fast != None and fast.next != None:
            slow = slow.next           # Move forward by 1 step  (x1)
            fast = fast.next.next      # Move forward by 2 steps (x2)
            if slow == fast:
                return True

        # If 'True'wasn't returned in the loop, means that there is no Loop
        return False