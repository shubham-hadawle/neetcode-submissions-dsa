# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Finding the middle of the LL (Fast & Slow Pointers)
        slow, fast = head, head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        second_half_head = slow.next
        slow.next = None

        # 2. Reversing the second half
        prev, curr = None, second_half_head
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        reversed_head = prev

        # 3. Merge the 2 halves in alternating order
        first, second = head, reversed_head
        
        while second != None:   # NOTE: second half LL will always be smaller or equal to the first half
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

        # return head