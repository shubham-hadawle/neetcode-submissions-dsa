# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge Case - list is empty or only a single element
        if lists is None or len(lists) == 0:
            return None

        while len(lists) > 1:
            merging_stage = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                merging_stage.append(self.merge2Lists(l1, l2))
            lists = merging_stage
        return lists[0]     # The 0th Position will return the head of the Final LL

    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        curr = dummy

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        if l1 != None:
            curr.next = l1
        elif l2 != None:
            curr.next = l2

        return dummy.next               