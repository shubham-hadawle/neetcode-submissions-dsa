# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # STEP 1: Finding the Middle
        slow, fast = head, head.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        # STEP 2: Reverse the Second Half
        prev, curr = None, slow.next
        slow.next = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        reverse_head = prev

        # STEP 3: Merge the Two Halves
        first, second = head, reverse_head
        while second != None:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2