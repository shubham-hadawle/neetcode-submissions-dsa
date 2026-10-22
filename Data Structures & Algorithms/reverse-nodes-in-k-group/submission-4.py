# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy

        while True:
            kthNode = self.getkthNode(groupPrev, k)
            if kthNode == None:
                    break
            groupNext = kthNode.next
            prev, curr = groupNext, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            first_to_last = groupPrev.next
            groupPrev.next = kthNode
            groupPrev = first_to_last

        return dummy.next                

    def getkthNode(self, curr, k):
        while curr != None and k > 0:
            curr = curr.next
            k -= 1
        return curr