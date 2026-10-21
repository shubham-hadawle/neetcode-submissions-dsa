# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == None or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedTwo = self.mergeTwo(l1, l2)
                merged.append(mergedTwo)

            lists = merged

        return lists[0]

    def mergeTwo(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                curr.next = l1
                curr = l1
                l1 = l1.next
            else:
                curr.next = l2
                curr = l2
                l2 = l2.next

        if l1 != None:
            curr.next = l1
        if l2 != None:
            curr.next = l2

        return dummy.next