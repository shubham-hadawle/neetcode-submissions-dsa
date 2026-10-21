class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # STEP 1: Fast & Slow Pointers
        # STEP 2: Two Slow Pointers

        head = 0
        first_intersection = 0
        fast, slow = head, head

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                first_intersection = slow
                break

        slow1, slow2 = head, first_intersection
        while slow1 != slow2:
            slow1 = nums[slow1]
            slow2 = nums[slow2]

        return slow1