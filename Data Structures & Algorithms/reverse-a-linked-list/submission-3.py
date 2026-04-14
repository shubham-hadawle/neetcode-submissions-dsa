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
        # # Iterative Way - Time: O(n), Space: O(1)
        # curr = head
        # prev = None

        # while curr != None:
        #     tempNext = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = tempNext
        #     # print(prev.val)

        # return prev

        # Recursive - Time: O(n), Space: O(1)
        # If the LL is empty or has only 1 node, return the head as it is
        if head is None or head.next is None:
            return head

        new_head = head
        if head.next is not None:
            new_head = self.reverseList(head.next)
            temp = head.next
            temp.next = head
        head.next = None
        return new_head