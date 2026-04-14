# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        behind, ahead = dummy, dummy

        # Set 'ahead' pointer at a position (n+1) steps ahead of 'behind'
        for i in range(0, n+1):
            ahead = ahead.next

        while ahead != None:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next

        return dummy.next