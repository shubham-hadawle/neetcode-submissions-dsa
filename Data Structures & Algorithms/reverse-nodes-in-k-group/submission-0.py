# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)   # Note this
        groupPrev = dummy   # Note this

        # Check and get the prescence of kth Node
        while True:
            kth = self.getKthNode(groupPrev, k)
            if kth == None:
                break
            groupNext = kth.next

            # Reversing the subGroup
            prev, curr = kth.next, groupPrev.next   # Note this
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Linking
            temp2 =  groupPrev.next
            groupPrev.next = kth
            groupPrev = temp2

        return dummy.next

    def getKthNode(self, curr, k):
        while curr != None and k > 0:
            curr = curr.next
            k -= 1
        return curr
