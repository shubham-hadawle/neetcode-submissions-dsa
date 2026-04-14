# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Way - Time: O(n), Space: O(1)
        curr = head
        prev = None

        while curr != None:
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
            # print(prev.val)

        return prev